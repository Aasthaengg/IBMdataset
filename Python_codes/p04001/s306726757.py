s=input()
ans=0
l=len(s)
num=2**(l-1)
for i in range(num):
    now=s[0]
    for j in range(l-1):
        if (i>>j)&1==1:
            ans+=eval(now)
            now=s[j+1]
        else:
            now+=s[j+1]
    ans+=eval(now)
print(ans)