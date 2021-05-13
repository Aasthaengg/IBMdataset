A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = min(a) + min(b)

c_min = 200001
for _ in range(M):
    x, y, c = map(int, input().split())
    c_min = min(c_min, a[x-1] + b[y-1] - c)

result = min(s, c_min)
print(result)