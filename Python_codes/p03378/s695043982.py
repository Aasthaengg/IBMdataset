N, M, X = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(M):
    if a[i] < X:
        cnt += 1
    else:
        break
if cnt > M - cnt:
    cnt = M - cnt

print (cnt)