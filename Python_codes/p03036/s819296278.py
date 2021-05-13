r, d, x = map(int, input().split())
cnt = 0

while cnt < 10:
    x = r*x-d
    print(x)
    cnt += 1