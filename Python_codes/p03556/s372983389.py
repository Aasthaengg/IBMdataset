N = int(input())
if N == 1:
  print(1)
  quit()

pre = 0
for i in range(1, N+1):
  n = i**2
  if n > N:
    print(pre)
    quit()
  
  pre = n