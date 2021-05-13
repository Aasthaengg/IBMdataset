a, b, c = [int(i) for i in input().split()]
if a == b == c and a % 2 == 0:
    print(-1)
    exit()
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(0)
    exit()
cnt = 0
while True:
    ta, tb, tc = a, b, c
    ta = (b + c) // 2
    tb = (a + c) // 2
    tc = (a + b) // 2
    cnt += 1
    if ta % 2 == 1 or tb % 2 == 1 or tc % 2 == 1:
        print(cnt)
        break
    a, b, c = ta, tb ,tc