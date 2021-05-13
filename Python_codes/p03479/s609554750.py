X,Y = map(int,input().split())

cnt = 0
while True:
    if X > Y:
        break
    X = X*2
    cnt += 1
print(cnt)