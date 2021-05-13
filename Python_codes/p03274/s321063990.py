n,k=map(int,input().split())
x=list(map(int,input().split()))
ans=float("inf")
for i in range(n-k+1):
    l=x[i]
    r=x[i+k-1]
    if l*r==0:
        t=max(abs(l),abs(r))
    if l*r>0:
        t=max(abs(l),abs(r))
    if l*r<0:
        if abs(l)>abs(r):
            t=2*abs(r)+abs(l)
        if abs(r)>=abs(l):
            t=2*abs(l)+abs(r)
    if t<ans:
        ans=t
print(ans)