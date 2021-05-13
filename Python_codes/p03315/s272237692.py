S=str(input())
k = 0
for i in range(4):
  if S[i] == '+':
    k = k + 1
  else:
    k = k - 1
print(k)
