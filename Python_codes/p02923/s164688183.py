N = int(input())
*A, = map(int, input().split())
ans = 0
cnt = 0
pre = -1
for a in A:
    if pre < a:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1
    pre = a
ans = max(ans, cnt)
print(ans)
