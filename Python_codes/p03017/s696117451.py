N, A, B, C, D = map(int, input().split())
S = input()
p = 0
t = 0
stri = 0
for i in range(A-1, max(C, D) - 1):
  if S[i:i+2] == '##':
    p = 1
for j in range(B-1, min(C, D) - 1):  
  if S[j:j+3] == '...':
    if stri == 0:
      stri = j + 1
    t = 1
if S[B] == '.' and S[B-2] == '.':
  t = 1
if (C < D and p == 0) or (C > D and p == 0 and t == 1 and stri <= D-1):
  print('Yes')
else:
  print('No')