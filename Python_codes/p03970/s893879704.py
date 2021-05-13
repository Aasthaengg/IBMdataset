S = input()
counter = 0
base ='CODEFESTIVAL2016'
for i in range(len(S)):
  if S[i] != base[i]:
    counter += 1
print(counter)
