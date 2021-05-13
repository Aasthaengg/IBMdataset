S = input()
T = input()
x,y = len(S),len(T)
A = [0] * (x-y+1)
for i in range(0, x-y+1):
  count = 0
  j = 0
  for k in range(i, i+y):
    if S[k] != T[j]:
      count += 1
    j += 1
  A[i] = count
print(min(A))