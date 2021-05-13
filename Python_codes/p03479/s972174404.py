x, y = [int(i) for i in input().split()]
n = x
cnt = 0
while n <= y:
    cnt += 1
    n *= 2
print(cnt)
