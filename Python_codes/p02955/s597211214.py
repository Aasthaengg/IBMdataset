from itertools import accumulate

def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return sorted(ass, reverse=True)

n,k = map(int, input().split())
a = list(map(int, input().split()))
div = divisor(sum(a))

for x in div:
    r = sorted([i%x for i in a])
    sr = sum(r)
    if sr == 0:
        print(x)
        exit()
    cr = list(accumulate(r))
    for i, j in enumerate(cr):
        if j == x*(n-i-1) - (sr-j) and j <= k:
            print(x)
            exit()