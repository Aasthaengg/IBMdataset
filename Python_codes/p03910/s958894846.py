n = int(input())

cnt = 0
pbm = 0
for i in range(1, 10**6):
    cnt += i
    if cnt >= n:
        pbm = i
        break

ans = []

for i in range(pbm, 0, -1):
    if i <= n:
        ans.append(i)
        n -= i

for i in ans:
    print(i)