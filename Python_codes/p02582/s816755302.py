S = input()
a = 0
for i in range(3):
  if S[i]=="R":
    a+=1
  if S[i]=="S" and a>0:
      break
print(a)