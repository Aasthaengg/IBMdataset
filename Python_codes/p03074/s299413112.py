n,k = map(int,input().split())
s = input()

cnt = [0]
now = '1'
for i in range(n):
    if(s[i]==now):
        cnt[-1] += 1
    else:
        now = s[i]
        cnt.append(1)
cnt = cnt + [0,0]

m = len(cnt)
if( m <= 2*k+1):
    print(n)
    exit()

l = 0
r = 2*k+1
tmp = sum(cnt[:r])
ans = tmp
while(r+2 <= m):
    tmp += cnt[r] + cnt[r+1] - cnt[l] - cnt[l+1]
    ans = max(ans,tmp)
    l += 2
    r += 2
print(ans)