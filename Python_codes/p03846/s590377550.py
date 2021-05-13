n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 2**(n//2)%mod
if n % 2 == 0:
    l = n ** 2
else:
    l = (n - 1) * (n + 1)
if sum(a) == l // 2:
    print(ans)
else:
    print(0)
