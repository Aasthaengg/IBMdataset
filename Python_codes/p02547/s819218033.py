N = int(input())
D = [tuple(map(int, input().split())) for _ in range(N)]
cnt = 0
for d1, d2 in D:
    if d1 == d2:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print('Yes')
        exit()
print('No')