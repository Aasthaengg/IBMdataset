N = int(input())
A = list(map(int,input().split()))

almost_half = sum(A)/2

former = 0
for n in range(N):
  former += A[n]
  if former == almost_half:
    print(0)
    break
    
  if former > almost_half:
    if n == 0:
      #print("case01",n,former)
      print(abs(A[0]-sum(A[1:])))
      break
    elif n == N-1:
      #print("case02",n,former)
      print(abs(A[n]-sum(A[:n])))
      break
    else:
      #print("case03",n,former)
      #print(abs(sum(A[n:])-sum(A[:n])),abs(sum(A[n+1:])-sum(A[:n+1])))
      print(min(abs(sum(A[n:])-sum(A[:n])),abs(sum(A[n+1:])-sum(A[:n+1]))))
      break