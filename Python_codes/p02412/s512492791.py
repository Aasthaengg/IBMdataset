while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    numbers = set()
    N = [i for i in range(1, n+1)]
    for i in N:
        for j in N:
            if i == j:
                break
            for k in N:
                if i == j or i == k or j == k:
                    break
                else:
                    numbers.add((i, j, k))
    count = 0
    numbers = list(numbers)
    for i in numbers:
        if i[0] + i[1] + i[2] == x:
            count += 1
    print(count)