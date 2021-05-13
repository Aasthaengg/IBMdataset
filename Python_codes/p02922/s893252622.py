a, b = map(int, input().split())

if b == 1:
    print(0)
    exit()

ans = a
cnt = 1
for i in range(50):
    if ans >= b:
        print(cnt)
        exit()
    ans += a -1
    cnt += 1
