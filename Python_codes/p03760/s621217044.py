o=input()
e=input()
ans=""
for i in range(len(o)-1):
  ans=ans+o[i]+e[i]
if len(o)!=len(e):
  print(ans+o[-1])
else:
  print(ans+o[-1]+e[-1])