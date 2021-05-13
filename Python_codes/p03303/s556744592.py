s=list(input())
n=int(input())


ans=''
for i in range(len(s)):
    if i*n<=len(s)-1:
        ans+=s[i*n]
print(ans)