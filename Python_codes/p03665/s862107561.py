from scipy.special import comb
n,p = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0,0] #偶数,奇数
for a in A:
    if a%2==0: cnt[0] += 1
    else: cnt[1] += 1
      
ans = 0
if p==0: #偶数＋奇数を偶数個(0個含む)
    for i in range(0,cnt[1]+1,2):
        ans += comb(cnt[1],i,exact=True)
    ans *= 2**cnt[0]
else: #偶数＋奇数を奇数個
    for i in range(1,cnt[1]+1,2):
        ans += comb(cnt[1],i,exact=True)
    ans *= 2**cnt[0]
print(ans)