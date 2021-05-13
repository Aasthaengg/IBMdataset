n, m, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    if a[i] >= x:
        idx = i
        break

print(min(i, m-i))