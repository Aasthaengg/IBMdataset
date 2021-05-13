def solve(args):
    n, y = args

    #.
    for i in range(n+1):
        for j in range(0, n-i+1):
            #.
            k = n - i - j

            #.
            if i*10000 + j*5000 + k*1000 == y:
                return "{} {} {}".format(i, j, k)

    return "-1 -1 -1"

print(solve(map(int, input().split())))
