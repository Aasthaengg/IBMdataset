s=input()
k=int(input())
ans=''
for c in s:
    t=ord('z')-ord(c)+1
    if t<26 and t<=k:
        k-=t
        ans+='a'
    else:
        ans+=c
if k>0:
    ans=ans[:-1]+chr(ord('a')+(ord(ans[-1])-ord('a')+k)%26)
print(ans)