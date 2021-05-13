n = int(input())
lh = [int(w) for w in input().split()]

ans = 0
t = 0
for i in range(1, n):
    # print(t, end=" ")
    if lh[i] <= lh[i - 1]:
        t += 1
        ans = max(ans, t)
    else:
        ans = max(ans, t)
        t = 0

print(ans)
