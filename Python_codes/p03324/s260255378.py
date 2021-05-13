d,n = map(int, input().split())
if n < 100:
    x = n * 100 ** d
else:
    x = 101 * 100 ** d
print(x)