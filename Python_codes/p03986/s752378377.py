x = input()
#tのラストとsの最初を知りたい
n = len(x)
a = []
for i in range(n):
  if x[i]=="S":
    a.append(x[i])
  else:
    if len(a)!=0 and a[-1]=='S' :
      a.pop()
    else:
      a.append(x[i])
print(len(a))