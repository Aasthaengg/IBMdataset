N = int(input())
ans = 0
for i in list(range(N+1))[1::2]:
    pre = 0
    for j in range(1, i + 1):
        if i % j == 0:
            pre += 1
    if pre == 8:
        ans += 1
print(ans)