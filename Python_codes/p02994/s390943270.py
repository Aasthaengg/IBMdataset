n, l = map(int, input().split())

a = []

for i in range(n):
    a.append(i+l)

print(sum(a) - min(a, key = abs))