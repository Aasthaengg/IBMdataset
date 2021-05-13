def solve(x):
    k = 1
    while k*x % 360 != 0:
        k += 1
    return k

x = int(input())
print(solve(x))