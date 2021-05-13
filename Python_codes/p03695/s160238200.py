n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 9
free = 0

for _a in a:
    r = _a//400
    if r < 8:
        cnt[r] = 1
    else:
        free += 1

if free == n:
    print(1, free)
else:
    print(sum(cnt), sum(cnt) + free)