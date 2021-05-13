k,s = map(int,input().split())

d = {}
cnt = 0
for x in range(k+1):
    for y in range(x+1):
        z = s - x - y
        if(z >= 0 and z <= y):
            if(x == y and y == z):
                cnt += 1
            elif(x == y or y == z or z == x):
                cnt += 3
            else:
                cnt += 6

print(cnt)

