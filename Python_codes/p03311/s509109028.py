N = int(input())
A = list(map(int, input().split()))
A = [a-i-1 for i, a in enumerate(A)]
A.sort()
if N%2:
  med = A[(N-1)//2]
  A = [abs(a-med) for a in A]
  print(sum(A))
  exit()
else:
  med1 = (A[N//2-1]+A[N//2])//2
  med2 = med1 + 1
  A1 = [abs(a-med1) for a in A]
  A2 = [abs(a-med2) for a in A]
  print(min(sum(A1), sum(A2)))
  exit()