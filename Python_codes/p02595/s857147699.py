n, d = map(int,input().split())

cnt = 0

for i in range(n):
    x, y = map(int,input().split())
    di = ((x ** 2) + (y ** 2)) ** (1/2)
    if di <= d:
        cnt += 1

print(cnt)