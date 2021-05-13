import bisect
N,X = map(int,input().split())
L =list(map(int,input().split()))
cnt = 0
M = [0]
for i in range(N):
    cnt += L[i]
    M.append(cnt)

print(bisect.bisect_right(M,X))