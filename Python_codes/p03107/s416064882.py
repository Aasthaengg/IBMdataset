S = input()
A = [0, 0]
for i in range(len(S)):
  if S[i] == "0":
    A[0] += 1
  else:
    A[1] += 1
print(2 * min(A))