MOD = 10**9 + 7
N = int(input())
cnt = 1
for i in range(N):
    cnt *= (i+1)
    cnt = cnt%MOD
print(cnt)