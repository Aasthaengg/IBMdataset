x,y = map(int,input().split())
a = y // x
for i in range(100):
    if 2 ** i > a:
        print(i)
        break