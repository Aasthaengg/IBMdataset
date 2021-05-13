n = int(input())
s = input()
mod = 10**9+7
cnt = {}
for x in s:
    if x not in cnt:cnt[x] = 1
    else:cnt[x] +=1
ans = 1
for key in cnt:
    v = cnt[key]
    ans *=(v+1)%mod
    ans %=mod
ans -= 1
print(ans)
