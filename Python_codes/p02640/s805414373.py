x,y = list(map(int,input().split()))
for crane in range(x+1):
    turtle = x - crane
    if y == crane*2 + turtle*4:
        print('Yes')
        break
else:
    print('No')