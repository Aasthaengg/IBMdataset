n,q=map(int,input().split())
t=input()
a=[0]*n
for i in range(n-1):
    if t[i]=="A"and t[i+1]=="C":
        a[i]=a[i-1]+1
    else:a[i]=a[i-1]
for _ in range(q):
    l,r=map(int,input().split())
    l,r=l-1,r-2
    print(a[r]-a[l-1])