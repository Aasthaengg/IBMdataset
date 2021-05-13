x,y = [int(x) for x in input().split()]

cnt = 0
while x <= y:
    x *= 2
    cnt += 1

print(cnt)