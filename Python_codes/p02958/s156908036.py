N = int(input())
P = list(map(int, input().split()))
P = [P[i]- (i+1) for i in range(N)]
if P.count(0) == N-2 or P.count(0) == N:
  print("YES")
else:
  print("NO")