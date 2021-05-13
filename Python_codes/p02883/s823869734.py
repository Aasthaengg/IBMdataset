def p_e():
    n, k = map(int, input().split())
    *A, = map(int, input().split())
    *F, = map(int, input().split())
    A.sort()
    F.sort(reverse=True)

    def check(x):
        count = 0
        for a, f in zip(A, F):
            count += max(a - x // f, 0)
        return count <= k

    max_num = 0
    for a, f in zip(A, F):
        if max_num < a * f:
            max_num = a * f
    l, h = 0, max_num
    while l <= h:
        mid = (l + h) // 2
        if check(mid):
            h = mid - 1
        else:
            l = mid + 1
    print(h + 1)
    
p_e()