S = input()
Z = 753
for i in range(3, len(S)+1):
  s = int(S[i-3:i])
  a = abs(753-s)
  if Z-a>0:
    Z = a
print(Z)