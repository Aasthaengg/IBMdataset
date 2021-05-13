n = int(input())
m = 100000

for i in range(n):
    m = 1.05 * m
    r = m % 1000
    if r > 0:
        m = (m // 1000 + 1) * 1000

print(int(m))