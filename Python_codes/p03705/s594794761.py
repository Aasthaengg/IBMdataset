N, A, B = map(int, input().split())

if A>B:
  print(0)
  exit()
elif N==1 and A!=B:
  print(0)
  exit()
else:
  ans = B*(N-1)+A - (B+A*(N-1))+1
  print(ans)