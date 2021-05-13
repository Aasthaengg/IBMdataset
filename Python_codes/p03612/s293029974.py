N = int(input())
pl = list(map(int, input().split()))

cnt = 0
for i in range(1,N):
    if pl[i-1] == i:
        a = pl[i - 1]
        pl[i - 1] = pl[i]
        pl[i] = a
        cnt += 1
if pl[N-1] == N:
    cnt += 1
print(cnt)
