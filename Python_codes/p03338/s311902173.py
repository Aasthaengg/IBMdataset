n=int(input())
s=input()
ans=0
for i in range(n-1):
    ls=set(s[0:i+1])
    rs=set(s[i+1:n])
    cnt=0
    for l in ls:
        if l in rs:
            cnt+=1
    ans=max(cnt,ans)
print(ans)