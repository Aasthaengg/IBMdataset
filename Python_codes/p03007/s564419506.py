import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()
if N == 2:
  print(A[1]-A[0])
  print(A[1],A[0])
  exit()
i0 = bisect.bisect_left(A,0)
if i0 >= N-1:
  print(-sum(A[:N-1])+A[N-1])
  a = A[N-1]
  for i in range(N-1):
    print(a,A[i])
    a = a-A[i]
elif i0 <= 1:
  print(-A[0]+sum(A[1:]))
  a = A[0]
  for i in range(1,N-1):
    print(a,A[i])
    a = a-A[i]
  print(A[N-1],a)
else:
  print(-sum(A[:i0])+sum(A[i0:]))
  a = A[i0-1]
  for i in range(i0,N-1):
    print(a,A[i])
    a = a-A[i]
  print(A[N-1],a)
  a = A[N-1]-a
  for i in range(i0-1):
    print(a,A[i])
    a = a-A[i]
