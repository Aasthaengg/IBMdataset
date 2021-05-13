n,m,k=map(int,input().split())
if(k>=m-n):
    for i in range(n,m+1):
        print(i)
else:
    l=list(range(n,n+k))
    d=list(range(m-k+1,m+1))
    s=l+d
    s=list(set(s))
    s.sort()
    for i in s:
        print(i)
