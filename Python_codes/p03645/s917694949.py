N,M = map(int,input().split())
x = set()
y = set()
 
for m in range(M):
    a,b = map(int,input().split())
    if a==1:
        x.add(b)
    if b==N:
        y.add(a)

if x&y:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")