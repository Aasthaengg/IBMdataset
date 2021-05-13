N = int(input())
A = list(map(int,input().split()))

cnt = 0
prev = A[0]
ans = 0
for i in range(1,N):
    if prev >= A[i]:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
    prev = A[i]

ans = max(ans,cnt)
print(ans)
