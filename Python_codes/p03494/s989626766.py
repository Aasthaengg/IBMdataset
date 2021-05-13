N = int(input())
A = list(map(int, input().split()))
 
count = 0
flag = False
while True:
  for n in range(N):
    if A[n] % 2 != 0:
      flag = True
      break
  if flag: break
  
  for n in range(N):
    A[n] //= 2
  count += 1

print(count)