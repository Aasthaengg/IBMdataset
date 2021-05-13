N,M,X = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for i in range(M):
    if X>A[i]:
        cnt += 1
print(min(cnt,M-cnt))