import itertools
while(True):
    n, x = [int(i) for i in input().split()]
    if n == 0 and x == 0: break
    cnt = 0
    for li in itertools.combinations(range(1, n + 1),3):
        if sum(li) == x: cnt += 1
    print(cnt)