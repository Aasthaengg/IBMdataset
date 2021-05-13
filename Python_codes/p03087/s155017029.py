n,q = map(int, input().split())
s=input()
a=[0]*n
for i in range(1,n):
    a[i]+=a[i-1]
    if s[i-1]=='A' and s[i]=='C':
        a[i]+=1
for i in range(q):
    l,r=map(int, input().split())
    print(a[r-1]-a[l-1])
