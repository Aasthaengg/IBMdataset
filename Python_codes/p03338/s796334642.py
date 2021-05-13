n=int(input())
s=input()
ans=0
for i in range(1,n):
    cnt=0
    a=list(set(list(s[0:i])))
    b=list(set(list(s[i:n])))
    if len(a)<len(b):
        for j in range(len(a)):
            if a[j] in b:
                cnt+=1
        ans=max(ans,cnt)
    else:
        for j in range(len(b)):
            if b[j] in a:
                cnt+=1
        ans=max(ans,cnt)
print(ans)