A,B,C = map(int,input().split())
count = 0
while A%2 == 0 and B%2 == 0 and C%2 == 0 and count < 10**5:
  A_copy = A
  B_copy = B
  A = (B+C)/2
  B =(A_copy+C)/2
  C = (A_copy+B_copy)/2
  count += 1
if count == 10**5:
  print(-1)
else:
  print(count)