N = int(input())
P = list(map(int, input().split()))
Q = sorted(P)
ans = 0
for i in range(len(P)):
  if P[i] != Q[i]:
    ans += 1
if ans > 2:
  print("NO")
else:
  print("YES")
