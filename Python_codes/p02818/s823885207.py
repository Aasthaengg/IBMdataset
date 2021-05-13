a, b, k = [int(x) for x in input().split()]

d = min(a, k)
a -= d
k -= d
b = max(0, b - k)
print(a, b)