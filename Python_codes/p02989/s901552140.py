n = int(input())
d = list(map(int, input().split()))
d.sort()
m = n // 2
m = d[m] - d[m - 1]
print(m)