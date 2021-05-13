n, m = map(int, input().split())
apple = []
for _ in range(n):
    apple.append(list(map(int, input().split())))
apple = sorted(apple)
msum = 0
ans = 0
for i in apple:
    msum += i[1]
    if msum < m:
        ans += (i[0]*i[1])
    elif msum == m:
        ans += (i[0]*i[1])
        break
    else:
        a = m - (msum - i[1])
        ans += (i[0]*a)
        break
print(ans)