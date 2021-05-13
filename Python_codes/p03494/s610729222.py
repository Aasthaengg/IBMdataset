N = int(input())
A = list(map(int,input().split()))

cnt = 0
check = True
while check:
  for i in range(N):
    if A[i] % 2 == 1:
      check = False
      break
    else:
      A[i] //= 2
  else:
    cnt += 1
    
print(cnt)