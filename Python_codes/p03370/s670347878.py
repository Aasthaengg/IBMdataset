n, x = map(int, input().split())

m = list()

for a in range(0, n):
    m.append(int(input()))

s = sum(m)

print(n + (x - s) // min(m))
