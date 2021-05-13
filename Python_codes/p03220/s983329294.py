n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

inf = float('inf')
closest = inf
closest_i = inf
for i, v in enumerate(h):
    if abs(a - (t - 0.006*v)) < closest:
        closest = abs(a - (t - 0.006*v))
        closest_i = i + 1
print(closest_i)