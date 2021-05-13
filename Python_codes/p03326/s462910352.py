n,m = map(int, input().split())
# x,y,z=[],[],[]
xyz = []
for _ in range(n):
    a,b,c = map(int, input().split())
    xyz.append((a,b,c))

ans = 0
for i in range(8):
    a,b,c = (-1)**(i&4 > 0), (-1)**(i&2 > 0), (-1)**(i&1 > 0)
    xyz.sort(key=lambda x:a*x[0] + b*x[1] + c*x[2], reverse=True)
    x,y,z=0,0,0
    for i in range(m):
        a,b,c = xyz[i]
        x += a
        y += b
        z += c
    tmp = abs(x) + abs(y) + abs(z)
    #print(tmp, ans)
    if ans < tmp:
        ans = tmp
print(ans)
