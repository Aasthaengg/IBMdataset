from itertools import combinations
n, k = map(int, input().split())


MAX_PAIR = (n-1)*(n-2)//2
if MAX_PAIR < k:
    print(-1)
else:
    m = n-1+MAX_PAIR-k
    print(m)
    for v2 in range(2, n+1):
        print(1, v2)

    cnt = MAX_PAIR-k
    for v, v2 in combinations(range(2, n+1), 2):
        if cnt == 0:
            break
        cnt -= 1
        print(v, v2)