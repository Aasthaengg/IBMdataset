n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
AB.sort(key=lambda x: [x[1]])
migi = 0
cnt = 0
for i in range(m):
    a, b = AB[i]
    if migi <= a:
        cnt += 1
        migi = b

print(cnt)
