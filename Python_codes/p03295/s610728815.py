N,M=map(int, input().split())
L=[]
for i in range(M):
    a,b=map(int, input().split())
    L.append((b,a))

L=sorted(L)
preb=0
ans=0
for l in L:
    b,a=l
    if preb<=a:
        ans+=1
        preb=b
print(ans)