N,A,B = map(int,input().split())

if N < 1 or B - A < 0:
  print(0)
  exit(0)
  
if N == 1 and A < B:
  print(0)
  exit(0)
  
  
if A == B or N <= 2:
  print(1)
  exit(0)
  
c = N-2
r = B-A+1

ans = c*(r-1) + 1
print(ans)

