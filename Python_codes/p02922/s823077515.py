A,B = map(int, input().split())
if B == 1:
  print(0)
  exit(0)
  
sumA = A
if sumA >= B:
  print(1)
  exit(0)

sumA = sumA + A - 1
for i in range(2,100):
  if sumA >= B:
    print(i)
    break
  else:
    sumA = sumA + A - 1