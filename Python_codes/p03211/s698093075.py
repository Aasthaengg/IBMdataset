s=input()
ans=1000
for i in range(len(s)-2):
    n=''
    n+=s[i]
    n+=s[i+1]
    n+=s[i+2]
    n=int(n)
    ans=min(abs(n-753),ans)
print(ans)