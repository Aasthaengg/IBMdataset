def resolve():
    n = int(input())
    a = []

    for i in range(n):
        row = list(map(lambda x: int(x) - 1, input().split()))
        row.reverse()
        a.append(row)

    q = set()

    def check(i):
        if len(a[i]) == 0:
            return
        j = a[i][-1]
        if i == a[j][-1]:
            p = (i, j) if i < j else (j, i)
            q.add(p)

    for i in range(n):
        check(i)

    day = 0
    while len(q) > 0:
        day += 1
        prev_q, q = q, set()

        for p in prev_q:
            (i, j) = p
            a[i].pop()
            a[j].pop()

        for p in prev_q:
            (i, j) = p
            check(i)
            check(j)

    for i in range(n):
        if len(a[i]) != 0:
            print(-1)
            return
    print(day)
    
resolve()
