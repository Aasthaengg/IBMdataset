S = input ()
A = 'CODEFESTIVAL2016'
x = 0
for i in range (16):
  if S[i] != A[i]:
    x += 1
print (x)