o=list(input())
e=list(input())
if len(o)!=len(e):
  e.append("")
ret=""
for (x,y)in zip(o,e):
  ret+=x+y

print(ret)