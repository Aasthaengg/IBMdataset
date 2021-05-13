A = [int(input()) for i in range(5)]
ans =643

for n in range(5):
  S = 0
  A = [A[4]]+A[:4]
  for a in A[:4]:
    S += -(-a//10)*10
  ans = min(ans,S+A[4])
  
print(ans)