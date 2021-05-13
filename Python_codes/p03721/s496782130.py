n,k = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n)]
s_ab = sorted(ab, key=lambda x: x[0])
cnt = 0
ans = -1
for i in s_ab:
    cnt += i[1]
    if cnt >= k:
        ans = i[0]
        break
print(ans)