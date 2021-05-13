n=int(input())
s=list(input())
num=[0]*26
for i in range(n):
    num[ord(s[i])-97]+=1
ans=1
for i in range(26):
    ans*=num[i]+1
    ans%=10**9+7
ans-=1
ans%=10**9+7
print(ans)
