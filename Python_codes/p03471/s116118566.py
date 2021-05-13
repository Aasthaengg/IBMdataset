n,y = map(int,input().split())
y //= 1000
f = 0
for s in range(n+1):
    for t in range(n+1-s):
        if s+t*5+(n-s-t)*10 == y:
            f = 1
            print(n-s-t,t,s)
            break
    if f == 1:
        break
else:
    print(-1,-1,-1)