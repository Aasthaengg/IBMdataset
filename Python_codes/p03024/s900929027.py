S = input()
kazu = 0
for i in range(len(S)):
  if(S[i]=="o"):
    kazu +=1
if(kazu+15-len(S)>=8):
  print("YES")
else:
  print("NO")