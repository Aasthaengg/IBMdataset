N = int(input())

Work = [tuple(map(int, input().split()))for _ in range(N)]

Work.sort(key=lambda x: x[1])
now = 0
for a, b in Work:
    now += a
    if b < now:
        print('No')
        exit()
print('Yes')