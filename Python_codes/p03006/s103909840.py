n = int(input())
d = dict()
p = []
for i in range(n):
    x,y = map(int,input().split())
    for j in p:
        if str(x-j[0])+" "+str(y-j[1]) in d:
            d[str(x-j[0])+" "+str(y-j[1])] += 1
        else:
            d[str(x-j[0])+" "+str(y-j[1])] = 1
        if str(j[0]-x)+" "+str(j[1]-y) in d:
            d[str(j[0]-x)+" "+str(j[1]-y)] += 1
        else:
            d[str(j[0]-x)+" "+str(j[1]-y)] = 1
    p.append([x,y])

if len(d.values()) == 0:
    ans = 0
else:
    ans = max(d.values())
print(n-ans)
