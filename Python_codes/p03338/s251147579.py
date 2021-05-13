n=int(input())
s=input()
ans=0
for i in range(1,n-1):
    tmp=0
    sa=list(s[:i])
    sa=set(sa)
    sa=list(sa)
    sb=list(s[i:])
    for j in range(len(sa)):
        if sa[j] in sb:
            tmp+=1
    if tmp>ans:
        ans=tmp
print(ans)