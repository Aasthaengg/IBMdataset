n, t = map(int, input().split())
a = [int(x) for x in input().split()]

lowest = a[0]
d = []

for i in range(n):
    d.append(a[i]-lowest)
    lowest = min(lowest, a[i])

print(d.count(max(d)))