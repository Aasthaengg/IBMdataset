h,w = map(int,input().split())

z = []
p = []
m = 10**9+7
for i in range(h):
    z.append(list(input()))
    p.append(list([0]*w))
p[0][0] = 1

for x in range(h):
    for y in range(w):
        if x != 0 or y != 0:
            if z[x][y] == "#":
                p[x][y] == 0
            else:
                p[x][y] += (p[x-1][y] + p[x][y-1])%m
               
                
print(p[h-1][w-1])