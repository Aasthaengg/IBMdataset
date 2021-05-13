N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
  ans = -1
else:
  minus = 0
  plus = []
  for i in range(N):
    dif = A[i] - B[i]
    if dif < 0:
      minus -= dif
    else:
      plus.append(dif)
   
  plus.sort(reverse=True)
  if minus <= 0:
    ans = 0
  else:
    for i in range(len(plus)):
      minus -= plus[i]
      if minus <= 0:
        break
    ans = N-len(plus)+i+1
print(ans)