n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
ans = 0
for d1, d2 in d:
    if d1 == d2:
        cnt += 1
        if cnt >= 3:
            print('Yes')
            exit()
    else:
        cnt = 0

print('No')