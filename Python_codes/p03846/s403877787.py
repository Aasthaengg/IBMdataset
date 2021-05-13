n = int(input())
a = list(map(int,input().split()))

from collections import Counter
MOD = 10**9 + 7
c = Counter(a)

ans = 0

if n % 2 == 1:
    for i in range(2, n, 2):
        if c[i] != 2:
            print(0)
            exit()
    if c[0] == 1:
        ans = pow(2, n // 2, MOD)
else:
    for i in range(1, n, 2):
        if c[i] != 2:
            print(0)
            exit()
    ans = pow(2, n // 2, MOD)
print(ans)
