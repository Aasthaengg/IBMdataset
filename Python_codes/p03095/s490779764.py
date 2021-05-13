n=int(input())
s=input()
mod = 1e9+7
ans = [1]*30
for c in s:
    ans[ord(c)-ord('a')]+=1
res = 1
for i in range(29):
    res *= ans[i]
    res %= mod
print(int((res-1)%mod))