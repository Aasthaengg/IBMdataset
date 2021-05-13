N = int(input())
A = list(map(int,input().split()))
flag = False

for i in range(1,max(A)):
  a = 2 ** i
  for n in range(N):
    if A[n] % a != 0:
      flag = True
      break
  if flag:
    break
    
print(i-1)