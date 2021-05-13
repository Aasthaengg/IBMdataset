from itertools import combinations
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    cnt = 0
    for li in combinations(range(1, n + 1), 3):
        if sum(li) == x:
            cnt += 1
    print(cnt)

