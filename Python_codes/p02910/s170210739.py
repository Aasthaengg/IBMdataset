S=input()
so=[]
se=[]
for i in range(len(S)):
  if i%2==1:
    se.append(S[i])
  else:
    so.append(S[i])
if (se.count("R")+so.count("L"))==0:
  print("Yes")
else:
  print("No")
