N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0

for i in range(N):
    if a[i] <= x:
        x -= a[i]
        cnt += 1
    else:
        break

if cnt == N and x!=0:
    cnt -=1

print(cnt)
