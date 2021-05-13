n,  k = list(map(int, input().split()))
al = list(map(int, input().split()))
cnt = [0]*n*2
dif = [0]*n
MOD = 10**9+7

al = al + al
for i in range(len(al)-1):
    for j in range(i+1, len(al)):
        if al[j] < al[i]:
            cnt[i] += 1

for i in range(n):
    dif[i] = cnt[i] - cnt[i+n]
print((sum(cnt[n:])*k + sum(dif)*(1+k-1)*(k-1)//2) % MOD)
