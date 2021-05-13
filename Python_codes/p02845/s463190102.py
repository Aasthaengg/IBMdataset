N = int(input())
A = map(int, input().split())
num = {i:0 for i in range(N+1)}
num[0] = 3
ans = 1
MOD = 1000000007
for a in A:
    ans *= num[a] % MOD
    num[a] -= 1
    num[a+1] += 1
print(ans%MOD)