n = int(input())
d = [0] * n
ans = 1
for i in range(n):
    d[i] = int(input())
d.sort()
for i in range(1, n):
    if d[i - 1] == d[i]:
        continue
    else:
        ans += 1
print(ans)
