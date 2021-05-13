n = int(input())
H = list(map(int, input().split()))

ans = 0
H_r = H[::-1]
cnt = 0

for i in range(n - 1):
    now = H_r[i]
    nex = H_r[i + 1]
    if now <= nex:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
    nex = now
print(ans)
