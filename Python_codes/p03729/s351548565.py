A, B, C = input().split()
Answer = 'NO'

if A[-1] == B[0] and B[-1] == C[0]:
  Answer = 'YES'

print(Answer)