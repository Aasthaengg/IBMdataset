n,k=map(int,input().split())
a=list(map(int,input().split()))
t={1:0}
g={0:1}
c,d=1,0
while d!=k:
    d+=1
    c=a[c-1]
    if c in t:
        print(g[t[c]+(k-t[c])%(d-t[c])])
        exit()
    else:
        t[c]=d
        g[d]=c
print(c)