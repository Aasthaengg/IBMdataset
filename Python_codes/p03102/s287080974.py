n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
cnt = 0

for l in a:
    tmp = 0
    for i in range(m):
        tmp += b[i]*l[i]
    tmp += c
    if tmp > 0:
        cnt += 1

print(cnt)