n = int(input())
s = input()
mod = 1000000007
alphacnt = [0]*26
ans = 0
for c in s:
    idx = ord(c)-ord("a")
    alphacnt[idx] += 1
    cnt = 1
    for i in range(26):
        if i == idx: continue
        cnt = (cnt*(alphacnt[i]+1))%mod
    ans = (ans+cnt)%mod
print(ans)