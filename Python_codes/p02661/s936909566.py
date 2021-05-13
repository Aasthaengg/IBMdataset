n = int(input())

v1, v2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    v1.append(a)
    v2.append(b)
v1.sort()
v2.sort()

if n & 1:
    m = n // 2
    print(v2[m] - v1[m] + 1)
else:
    m = n // 2
    print(v2[m-1]-v1[m-1] + v2[m]-v1[m] + 1)