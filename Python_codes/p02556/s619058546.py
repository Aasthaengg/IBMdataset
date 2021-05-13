n = int(input())
p = []
m = []
for i in range(n):
    x,y = map(int,input().split())
    p.append(x+y)
    m.append(x-y)
p.sort()
m.sort()
print(max(p[-1]-p[0],m[-1]-m[0]))