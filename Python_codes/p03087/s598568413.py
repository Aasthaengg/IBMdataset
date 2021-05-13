n,q=map(int,input().split())
s=input()
L=[0 for i in range(n+1)]

for i in range(2,n+1):
    if s[i-1]=="C" and s[i-2]=="A":
        L[i]=L[i-1]+1
    else:
        L[i]=L[i-1]

for que in range(q):
    l,r=map(int,input().split())
    print(L[r]-L[l])