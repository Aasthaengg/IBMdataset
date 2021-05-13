N = int(input())
A = list(str(input()))
B = list(str(input()))
C = list(str(input()))

ans = 0
for i in range(N):
  if [A[i] == B[i], B[i] == C[i], C[i] == A[i]].count(False) == 2:
    ans +=  1
  elif [A[i] == B[i], B[i] == C[i], C[i] == A[i]].count(False) == 3:
    ans += 2
  else:
    pass
    
print(ans)
