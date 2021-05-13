n, h = map(int, input().split())
arr_a = []
arr_b = []
for _ in range(n):
    a, b = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)

max_a = max(arr_a)
arr_b.sort(reverse=True)

ans = 0
for b in filter(lambda x: x > max_a, arr_b):
    ans += 1
    h -= b
    if h <= 0:
        break
else:
    ans += 0 - -h//max_a

print(ans)
