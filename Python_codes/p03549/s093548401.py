[n,m] = [int(i) for i in input().split()]
x = (n-m) * 100 * (2**m)
x += m * (2 ** m) * 1900
print(x)
