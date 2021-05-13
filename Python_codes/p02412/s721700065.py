while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0:
        break

    count = 0
    limit = n if n < x else x
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if sum([a,b,c]) == x:
                    count += 1

    print(count)