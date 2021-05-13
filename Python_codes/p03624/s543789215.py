alpha="abcdefghijklmnopqrstuvwxyz"
S=input()
for i in range(len(alpha)) :
  if alpha[i] not in S :
    print(alpha[i])
    exit()
print("None")