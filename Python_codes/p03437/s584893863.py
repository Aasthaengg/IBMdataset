x,y = map(int,input().split())
for i in range(1,1000000):
    if (x*i) % y != 0:
        print(x*1)
        exit()
    if x*i >= 10**18:
        break
print("-1")