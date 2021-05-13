S = input()
R = 'CODEFESTIVAL2016'
k = 0
for i in range(len(S)):
  if (S[i] != R[i]):
    k += 1
print(k)