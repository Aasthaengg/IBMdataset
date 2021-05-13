X, Y = map(int, input().split())

cnt = 1
num = X
while num <= Y:
    num *= 2
    if(num > Y):
        break
    cnt += 1

print(cnt)