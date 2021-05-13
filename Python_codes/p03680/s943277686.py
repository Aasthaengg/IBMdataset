N = int(input())
A = [int(input()) for _ in range(N)]
A.insert(0,0)
hist = [0 for _ in range(N+1)]
a = 1
cnt = 0
hist[a] = 1
while True:
    cnt += 1
    a = A[a]
    if hist[a]==1:
        cnt = -1
        break
    hist[a] = 1
    if a==2:
        break
print(cnt)