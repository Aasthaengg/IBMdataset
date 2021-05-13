S = input()
K = "CODEFESTIVAL2016"
sum = 0
for i in range(len(S)):
  if S[i] != K[i]:
    sum += 1
print(sum)
