n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
cnt = 0
for i, a in enumerate(A):
    if i == 0:
        ans += a
        cnt += 1
    else:
        if n-1 - cnt >= 2:
            ans += a*2
            cnt += 2
        else:
            ans += a
            cnt += 1
    if cnt == n-1:
        break
print(ans)