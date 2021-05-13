A,B,C = map(int,input().split())
count = 0

if A == B and B == C and A%2 == 0:
  print(-1)

else:
  while True:
    if A%2 == 1 or B%2 == 1 or C%2 == 1:
      break
    else:
      A2 = A
      B2 = B
      C2 = C
      A = B2/2 + C2/2
      B = A2/2 + C2/2
      C = A2/2 + B2/2
      count += 1
  print(count)