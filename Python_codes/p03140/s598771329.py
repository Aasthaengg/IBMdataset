n = int(input())
a, b, c = input(), input(), input()
ans = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        continue
    if a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
        ans += 1
    else:
        ans += 2
print(ans)
