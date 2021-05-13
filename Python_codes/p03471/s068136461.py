N, Y = map(int, input().split())
flag = False

for x in range(N+1):
    if flag == True:
        break
    for y in range(N-x+1):
        if 10000*x + 5000*y + 1000*(N-x-y) == Y:
            print(x, y, N-x-y)
            flag = True
            break

if flag == False:
    print(-1, -1, -1)