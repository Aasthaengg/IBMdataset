o=input()
e=input()

ans=''
for i in range(len(e)):
  ans+=o[i]+e[i]
if len(o)>len(e):
  ans+=o[len(o)-1]
print(ans)