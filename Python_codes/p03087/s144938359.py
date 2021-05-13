n, q=map(int, input().split())
s=input()


z=[0]*n
count=0
for i in range(n):
    z[i]=count
    if s[i]=="A" and i<=n-2:
        if s[i+1]=="C":
            count+=1
            z[i]+=1

for i in range(q):
    l, r =map(int,input().split())
    #r文字目までのACの数-(l-1)文字目まで
    if l==1:
        ans=z[r-2]
    elif r-l==1:
        if s[l-1]=="A" and s[l]=="C":
            ans=1
        else:
            ans=0
    else:
        ans=z[r-2]-z[l-2]
    print(ans)
