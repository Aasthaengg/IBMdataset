N,Y = map(int,input().split())

flag = 0
for x in range(N+1):
    if flag > 0:
        break
    for y in range(N-x+1):
        z = N-x-y
        if 10000*x+5000*y+1000*z == Y and flag == 0:
            flag+=1
            print(x,y,z)
            break
            
if flag == 0:
    print('-1 -1 -1')