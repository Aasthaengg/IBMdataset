n = int(input())
a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

min_val = b[a.index(max(a))]
print(max(a) + min_val)