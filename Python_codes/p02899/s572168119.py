N = int(input())
A = list(map(int, input().split()))
B = [[] for i in range(N)]
for i in range(N):
  B[i] = [A[i], i+1]
B.sort()
ans = [0 for i in range(N)]
for i in range(N):
  ans[i] = B[i][1]
print(*ans)