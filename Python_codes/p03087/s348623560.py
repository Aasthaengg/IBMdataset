def Csum(a):
    b,c=[0],0
    for i in range(len(a)-1):
        c+=(a[i]=='A' and a[i+1]=='C')
        b.append(c)
    return b
n,q=map(int,input().split())
s=Csum(input())
for i in range(q):
    a,b=map(int,input().split())
    print(s[b-1]-s[a-1])