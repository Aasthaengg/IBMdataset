N=int(input())
s=str(N)
ans=0
ans=9*(len(s)-1)
ans+=(int(s[0])-1)

val=0
for i in range(len(s)):
    val+=int(s[i])

ans=max(ans,val)
print(ans)