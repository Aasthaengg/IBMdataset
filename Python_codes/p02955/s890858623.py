N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
s = sum(A)
flag = False
def make_divisors(n):
    divisors = []
    for i in range(int(n**0.5), 0, -1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return sorted(divisors, reverse=True)
divs = make_divisors(s)
for x in divs:
    if flag:
        break
    sortedA = sorted([a%x for a in A])
    sumA = sum(sortedA)
    index_len = len(sortedA)
    sump = 0
    for i, a in enumerate(sortedA):
        sump += a
        summ = x*(index_len - (i+1)) - (sumA - sump)
        if sump == summ and sump <= K:
            print(x)
            flag = True
            break

