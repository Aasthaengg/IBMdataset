def abc141c():
    n, k, q = map(int, input().split())
    cnt = [0] * n
    for _ in range(q):
        cnt[int(input())-1] += 1
    for item in cnt:
        if k - (q-item) > 0:
            print('Yes')
        else:
            print('No')
abc141c()