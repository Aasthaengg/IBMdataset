N = int(input())
A = [int(i) for i in input().split()]
A.insert(0,0)
A.append(0)
S = 0
for i in range(1,N+2):
  S += abs(A[i] - A[i-1])
for i in range(1,N+1):
  tmp = [A[i-1],A[i],A[i+1]]
  tmp.sort()
  ans = 0
  if tmp[1] == A[i]:
    ans = S
  elif tmp[2] == A[i]:
    ans = S- (tmp[2]-tmp[1])*2
  else:
    ans = S - (tmp[1]-tmp[0])*2
  print(ans)