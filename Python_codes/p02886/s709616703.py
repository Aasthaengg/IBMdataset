n = int(input())
d = [int(s) for s in input().split()]
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            ans += d[i] * d[j]
print(ans // 2)