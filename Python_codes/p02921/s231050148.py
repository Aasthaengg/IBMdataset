S = list(str(input()))
T = list(str(input()))
a = 0
for i in range(3):
  if S[i] == T[i]:
    a += 1
print(a)