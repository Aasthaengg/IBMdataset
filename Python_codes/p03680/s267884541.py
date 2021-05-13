N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())
now, cnt = 0, 0

for i in range(N):
    if now == 1:
        print(cnt)
        exit()
    else:
        now = a[now]-1
        cnt += 1
print(-1)