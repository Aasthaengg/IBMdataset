n = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if i + 2 > n:
        break
    x = sorted(P[i - 1:i + 2])
    if x[1] == P[i]:
        ans += 1
print(ans)

