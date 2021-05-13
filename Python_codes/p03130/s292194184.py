g=[0]*5
for _ in range(3):
    a,b=map(int,input().split())
    g[a]+=1
    g[b]+=1
if g.count(1)==2:
    print("YES")
else:
    print("NO")
