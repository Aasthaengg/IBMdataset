r, d , x = map(int, input().split())
cnt = 0
print(r * x - d)
while cnt <= 8:
    x = r * x - d
    print(r * x - d)
    cnt += 1