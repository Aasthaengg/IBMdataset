n = int(input())
p = list(map(int, input().split()))

l = []
cnt = 0
for i in range(n):
    if p[i] == i + 1:
        cnt += 1
    else:
        if cnt > 0:
            l.append(cnt)
            cnt = 0
if cnt > 0:
    l.append(cnt)
    cnt = 0

res = 0
for v in l:
    res += (v + 1) // 2

print(res)