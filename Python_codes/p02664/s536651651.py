t=input()
ans=""
n=len(t)
for i in range(n):
  if (t[i]=="?"):
    ans=ans+"D"
  else:
    ans=ans+t[i]
    
print(ans)