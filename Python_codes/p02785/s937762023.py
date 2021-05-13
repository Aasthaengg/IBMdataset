n,k = map(int,input().split())
P = list(map(int,input().split()))

c=0
P.sort( reverse=True )

if k>len(P):
    k=len(P)
for i in range(k):
    c+=1    

ans = sum(P[c:])

print(ans)
