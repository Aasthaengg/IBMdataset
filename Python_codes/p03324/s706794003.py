d, n = [int(x) for x in input().split()]

x = 100 ** d

if n == 100:
    n = 101

ans = n * x
print(ans)