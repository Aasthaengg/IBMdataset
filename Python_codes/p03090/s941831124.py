n = int(input())

if n % 2 == 0:
    pairs = [(i, n+1-i) for i in range(1, n//2+1)]
    x = len(pairs)
    if n == 4:
        print(4 * (x - 1))
        for i in range(2):
            for j in range(2):
                print(pairs[0][i], pairs[1][j])
    else:
        print(4 * x)
        for k in range(n//2):
            for i in range(2):
                for j in range(2):
                    print(pairs[k%x][i], pairs[(k+1)%x][j])

else:
    pairs = [(i, n-i) for i in range(1, n//2+1)]
    x = len(pairs)
    if n == 3:
        print(2)
        print(1, 3)
        print(2, 3)
    else:
        print(4 * x)
        for k in range(n//2-1):
            for i in range(2):
                for j in range(2):
                    print(pairs[k % x][i], pairs[(k+ 1) % x][j])
        print(n, pairs[0][0])
        print(n, pairs[0][1])
        print(n, pairs[-1][0])
        print(n, pairs[-1][1])