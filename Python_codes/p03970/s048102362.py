S = input()
T = "CODEFESTIVAL2016"
s = 0
for i,j in zip(S, T):
  if i == j:
    s += 1
print(16-s)