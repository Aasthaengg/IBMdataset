n = int(input())
lh = list(map(int, input().split()))

ans = 0
for i in range(1, max(lh)+1):
    if lh[0] >= i:
        cnt = 1
    else:
        cnt = 0
    j = 1
    while j < n:
        if lh[j-1] < i and lh[j] >= i:
            cnt += 1
        j += 1
    ans += cnt

print(ans)