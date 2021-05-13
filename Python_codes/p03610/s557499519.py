S = input()
k = ""
for i in range(len(S)):
  if i % 2 == 0:
    k += S[i]
print(k)
