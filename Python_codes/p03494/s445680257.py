N = int(input())
A = list(map(int, input().split()))

counter = 0
while True:
  hasOdd = 0
  for i in range(N):
    if A[i] % 2 == 1:
      hasOdd += 1

  if hasOdd > 0:
    break

  A = [i / 2 for i in A]
  counter += 1
print(str(counter))