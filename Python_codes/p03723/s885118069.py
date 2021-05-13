a, b, c = map(int, input().split())

if a % 2 == 0 and a == b == c:
    print(-1)
    exit()

cnt = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    cnt += 1
    aa = b // 2 + c // 2
    bb = c // 2 + a // 2
    cc = a // 2 + b // 2
    a = aa
    b = bb
    c = cc
print(cnt)
