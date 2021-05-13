a=input()
n=len(a)
S=n*(n-1)//2+1

l={}
for i in range(n):
    if a[i] in l:
        l[a[i]]+=1
    else:
        l[a[i]]=1

cnt=0
for i in l:
    if l[i]>1:
        cnt+=l[i]*(l[i]-1)//2

ans=S-cnt

print(ans)