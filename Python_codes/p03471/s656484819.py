N, SUM = map(int,input().split())
X = 10000
Y = 5000
Z = 1000
ans = [-1, -1, -1]
for x in range(N+1):
    for y in range(N+1):
        z = N-x-y
        if z<0:
            break
        if X*x+Y*y+Z*z==SUM:
            ans = [x,y,z]
            break
                
print(*ans)
