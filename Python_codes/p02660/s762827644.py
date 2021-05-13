from math import sqrt


N = int(input())
ans = 0
for d in range(2, int(sqrt(N)) + 1):
    if N % d == 0:
        i = 1
        while N % d**i == 0:
            ans += 1
            N //= d**i
            i += 1
        while N % d == 0:
            N //= d

if N > 1:
    ans += 1
print(ans)