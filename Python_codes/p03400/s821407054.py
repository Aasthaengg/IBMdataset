N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]
ans = X
for i in range(N):
  ans = ans + (D-1)//A[i] + 1
print(ans)