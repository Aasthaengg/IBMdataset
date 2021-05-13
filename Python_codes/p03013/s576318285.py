n , m = map(int, input().split())
lis = [int(input()) for _ in range(m)]
mod = 10**9+7

ans =[1] + [1] + [-1] * (n-1)

for i in lis:
    ans[i] = 0


for i in range(2, n+1):
    if ans[i] != 0:
        ans[i] = (ans[i-1] + ans[i-2]) % mod

print(ans[n])