n, k = map(int, input().split())
t = n // k
m = (n * 2) // k - t
if k % 2 == 1:
    print(t**3)
else:
    print(t**3 + m**3)