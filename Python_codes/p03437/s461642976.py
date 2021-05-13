x,y = map(int,input().split())
for i in range(100):
    if x*i % y != 0:
        print(x*i)
        break
else:
    print(-1)