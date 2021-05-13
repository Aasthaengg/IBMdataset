import itertools

N = int(input())

ans = [0] * (100**2)
for x, y, z in itertools.product(range(1, 101), repeat=3):
    n = x**2 + y**2 + z**2 + x * y + y * z + z * x
    if  n <= 100**2:
        ans[n - 1] += 1

for i in range(N):
    print(ans[i])