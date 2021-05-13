n = int(input())
a = sorted(map(int, input().split()))
b = [0] * (10 ** 6 + 1)
c = [False] * (10 ** 6 + 1)
for i in a:
    b[i] += 1
ans = 0
for i in range(1, 10 ** 6 + 1):
    if not b[i]:
        continue
    if b[i] == 1 and not c[i]:
        ans += 1
    for j in range(1, 10 ** 6 + 1):
        if i * j > 10 ** 6:
            break
        c[i * j] = True
print(ans)