N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()
for i in range(N):
    if K>A[i][1]:
      K -= A[i][1]
    else:
      ans = A[i][0]
      break
print(ans)