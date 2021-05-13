N = int(input())
G = []
for i in range(N):
    x,y = map(int,input().split())
    G.append([x,y])

a = -10**10
b = 10**10
c = -10**10
d = 10**10

for i in range(N):
    x = G[i][0]
    y = G[i][1]
    t = x+y
    u = x-y
    a = max(a,t)
    b = min(b,t)
    c = max(c,u)
    d = min(d,u)

#print(a,b,c,d)
ans = max(a-b,c-d)
print(ans)
