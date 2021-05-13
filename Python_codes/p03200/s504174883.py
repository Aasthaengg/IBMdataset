S = input()
Nb = 0
count = 0
for i in range(len(S)):
  if S[i] == "B":
    Nb+=1
  else:
    count+=Nb
print(count)