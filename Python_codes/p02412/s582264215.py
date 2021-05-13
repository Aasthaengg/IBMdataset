while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0:
        break
    count = 0
    for a in range(n if n < x else x, 2, -1):
        for b in range(a-1, 1, -1):
            if a + b > x:
                continue
            for c in range(b-1, 0, -1):
                s = a + b + c
                if s == x:
                    count += 1
                    break
                elif s < x:
                    break
    print(count)