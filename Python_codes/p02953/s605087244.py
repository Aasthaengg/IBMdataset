n = int(input())
h = list(map(int, input().split()))
maxx = 0
ans = 1
for i in range(n):
    if h[i] - maxx >= -1:
        maxx = max(h[i], maxx)
    else:
        ans = 0
print(["No", "Yes"][ans])
