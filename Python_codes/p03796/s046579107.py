n = int(input())
MOD = 10**9 + 7
cnt = 1
for i in range(1,n+1):
    cnt = cnt * i % MOD

print(cnt)