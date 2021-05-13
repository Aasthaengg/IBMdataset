x,y = map(int,input().split())
for c in range(2,1000000):
    if c * x % y != 0:
        print(c * x)
        break
else:
    print(-1)