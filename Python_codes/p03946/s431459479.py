n, t = map(int, input().split())
a = list(map(int, input().split()))

mini = 10**9+1
diff = 0
ans = 1
for i in range(n):
    if a[i] <= mini:
        mini = a[i]

    if diff == a[i] - mini:
        ans += 1
    elif diff < a[i] - mini:
        ans = 1
        diff = a[i] - mini
print(ans)
