
x,y = map(int, input().split())

temp = x
cnt = 0

while temp <= y:
    temp = temp*2
    cnt += 1

print(cnt)

