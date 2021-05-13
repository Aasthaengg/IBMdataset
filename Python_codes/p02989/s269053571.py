N = int(input())
D = list(map(int,input().split()))
D.sort()

M = N//2
ans = D[M] - D[M-1]

if D[M] == D[M-1]:
  ans = 0

print(ans)