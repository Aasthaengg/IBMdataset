X,Y = map(int,input().split())

cnt = 0

while X <= Y:
    X += X
    cnt += 1

print(cnt)