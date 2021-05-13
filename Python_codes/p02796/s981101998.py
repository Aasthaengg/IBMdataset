n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

d = [[a[i][0]-a[i][1],a[i][0]+a[i][1]] for i in range(n)]

d = sorted(d, key = lambda x: x[1])

b = -100000000000000000
c = 0


for i in range(n):
    if d[i][0] >= b:
        b = d[i][1]
        c = c + 1

print(c)
        
    
