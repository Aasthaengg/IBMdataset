ABC = list(map(int, input().split()))

cnt = 0

if (ABC[0] == ABC[1] == ABC[2]) and (ABC[0]%2 == ABC[1]%2 == ABC[2]%2 == 0):
    print(-1)
    exit()
else:
    while True:
        if ABC[0]%2 == ABC[1]%2 == ABC[2]%2 == 0:
            ABC[0], ABC[1], ABC[2] = (ABC[1]+ABC[2])//2, (ABC[0]+ABC[2])//2, (ABC[0]+ABC[1])//2
            cnt += 1
        else:
            break
 
print(cnt)