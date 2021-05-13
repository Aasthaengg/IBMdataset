n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

cnt = [0]*n
ans = 1

for i in a:
    if i>0: ans *= max(0,cnt[i-1] - cnt[i])
    cnt[i] += 1
    if cnt[i]>3:ans = 0
    ans %= mod

ans *= 3 if cnt[0]==1 else 6

print(ans%mod)
