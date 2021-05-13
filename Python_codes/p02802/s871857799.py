n,m = map(int,input().split())

maru = [0]*n
pena = [0]*n

for i in range(m):
    p,s = input().split()
    p = int(p)
    if s =="AC":
        maru[p-1] = 1
    else:
        if maru[p-1]==0:
            pena[p-1]+=1

penapena = [maru[i]*pena[i] for i in range(n)]

print(maru.count(1),sum(penapena))