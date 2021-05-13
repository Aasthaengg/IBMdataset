N,A,B = map(int,input().split())
if N == 1:
  if A != B:
    print(0)
    exit()
  else:
    print(1)
    exit()
if A>B:
  print(0)
  exit()
MIN = A*(N-1)+B
MAX = A+B*(N-1)
ans = MAX-MIN +1
print(ans)