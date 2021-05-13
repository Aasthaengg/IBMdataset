def I(): return int(input())
N = I()
K = I()
ans = 1
for _ in range(N):
    ans = min(ans*2,ans+K)
print(ans)
