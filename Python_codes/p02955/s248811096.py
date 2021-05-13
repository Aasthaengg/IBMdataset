from collections import deque
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse=1)
    return divisors

n,k = map(int,input().split())
a = list(map(int,input().split()))
S = sum(a)
for gcd in make_divisors(S):
    li = deque(sorted([x % gcd for x in a]))
    count = 0
    L = li.popleft()
    R = li.pop()
    while li:
        if L >= gcd-R:
            L -= gcd-R
            count += gcd-R
            R = li.pop()
        else:
            R += L
            count += L
            L = li.popleft()
    count += L
    if count <= k:
        print(gcd)
        exit()