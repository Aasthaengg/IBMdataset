n,m = map(int,input().split())
AB = []
CD = []
for i in range(n):
    a,b = map(int,input().split())
    AB.append([a,b])
for i in range(m):
    c,d = map(int,input().split())
    CD.append([c,d])

for st in range(n):
    ans = float("inf")
    for po in range(m):
        dist = abs(AB[st][0]-CD[po][0])+abs(AB[st][1]-CD[po][1])
        if ans > dist:
            ans = dist
            memo = po + 1
    print(memo)
