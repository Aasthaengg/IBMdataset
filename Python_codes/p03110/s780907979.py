n=int(input())
x=[""]*n
u=[""]*n
ans=0
for i in range(n):
  x[i],u[i]=input().split()
  if (u[i]=="JPY"):
    ans+=int(x[i])
  else:
    ans+=float(x[i])*380000.0
print(ans)