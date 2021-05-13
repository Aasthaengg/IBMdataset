n, x = map(int, input().split())
l = list(map(int, input().split()))
d = [0]
for i in range(1, n+1):
    d.append(d[i-1]+l[i-1])
cnt = 0
for j in d:
    if j <= x:
        cnt += 1
print(cnt)