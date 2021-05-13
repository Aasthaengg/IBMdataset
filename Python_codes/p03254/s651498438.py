N,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
count = 0
flag = True

for i in range(len(A)):
  if x - A[i] >= 0:
    x -= A[i]
    count += 1
  else:
    flag = False
    break
    
if x > 0 and flag:
  print(count-1)
else:
  print(count)