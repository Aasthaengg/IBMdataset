n, k, s = map(int, input().split())
a = [0] * n
for i in range(k):
    a[i] = s
if s == 1:
    s = 3
for i in range(k, n):
    a[i] = s - 1
print(a[0], end = "")
for i in a[1:]:
    print("", i, end = "")
print()
