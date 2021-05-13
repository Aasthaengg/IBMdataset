n = int(input())
ans = float('inf')
for i in range(1, n):
    a = i
    b = n-i
    m = len(str(a))
    l = len(str(b))
    cnt = 0
    for j in range(m):
        cnt += int(str(a)[j])
    for j in range(l):
        cnt += int(str(b)[j])
    ans = min(ans, cnt)

print(ans)

