A, B = map(int, input().split())

from collections import defaultdict
def factorization(n):
    d = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            d[i] = cnt
    if temp != 1:
        d[temp] = 1
    if len(d) == 0:
        d[n] = 1
    return d
ans = 0
d = factorization(A)
d[1] = 1
for x in d.keys():
    if B%x == 0:
        ans += 1
print(ans)