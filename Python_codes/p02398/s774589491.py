ans = 0
a = map(int, raw_input().split())
for i in range(a[0], a[1] + 1):
    if a[2] % i == 0:
        ans += 1
print(ans)