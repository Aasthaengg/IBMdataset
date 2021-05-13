N, Y = map(int, input().split())

check = 0
for x in range(0,N+1):
    for y in range(0,N+1-x):
        z = Y - 10000*x - 5000*y
        if z == (N - x - y)*1000:
            z = int(z/1000)
            print(x,y,z)
            check = 1
            break
        # for z in range(0,N+1-x-y):
        #     if 10000*x + 5000*y + 1000*z == Y:
        #         print(x,y,z)
        #         check = 1
        #         break
        # if check == 1:
        #     break
    if check == 1:
        break
if check == 0:
    print("-1 -1 -1")
