a,b,m = map(int,input().split())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))

cst = min(ai) + min(bi)

for i in range(m):
    x,y,c = map(int,input().split())
    if cst > ai[x-1]+bi[y-1]-c:
        cst = ai[x-1]+bi[y-1]-c

print(cst)
