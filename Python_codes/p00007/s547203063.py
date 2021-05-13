N = int(raw_input())

res = 100000
for i in range(N):
    res *= 1.05
    if res % 1000 > 0:
        res -= res % 1000
        res += 1000
print int(res)