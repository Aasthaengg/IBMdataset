import itertools

n, k = map(int, input().split())
if k > (n - 1) * (n - 2) // 2:
    print(-1)
else:
    tmp = (n - 1) * (n - 2) // 2
    tmp -= k
    print(n - 1 + tmp)
    for i in range(1, n):
        print(i, n)
    if tmp == 0:
        exit()
    for lst in itertools.combinations(range(1, n), 2):
        print(lst[0], lst[1])
        tmp -= 1
        if tmp == 0:
            break