x,y = map(int,input().split())

for i in range(1, 10**9):
    if x * i % y != 0:
        print(x*i)
        break
    if x*i <= 10**18:
        print(-1)
        break