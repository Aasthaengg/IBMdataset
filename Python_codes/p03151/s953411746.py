N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
if sum(A) < sum(B):
  print(-1)
  exit()

D = []
for i in range(N):
  D += [A[i]-B[i]]
D.sort()
M = 0
for i in range(N):
  if D[i] < 0:
    M += D[i]
    ans += 1
  else:
    break
for i in reversed(range(N)):
  if M >= 0:
    print(ans)
    break
  else:
    M += D[i]
    ans += 1
