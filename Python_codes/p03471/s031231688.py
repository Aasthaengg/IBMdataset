def func(n, yen):
    n += 1
    for x in range(n):
        for y in range(n-x):
            z = n - x - y - 1
            if (x+y+z) == n-1 and 10000*x + 5000*y + 1000*z == yen:
                comb = (x, y, z)
                print(" ".join([str(i) for i in comb]))
                return
    print("-1 -1 -1")
    return


n, y = map(int, input().split())
func(n, y)