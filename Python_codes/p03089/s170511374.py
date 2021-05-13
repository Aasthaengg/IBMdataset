import sys

N = int(input())
A = list(map(int,input().split()))

for n in range(N):
  if A[n] >  n+1:
    print(-1)
    sys.exit()

ans = []

while A != []:
  tmp = 0
  for p in range(len(A)):
    if A[p] == p+1:
      tmp = p
  ans.insert(0,A.pop(tmp))

  
for x in ans:
  print(x)