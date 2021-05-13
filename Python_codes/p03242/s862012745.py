n=input()
ans=""
for x in n:
  if x=="1":
    ans+="9"
  elif x=="9":
    ans+="1"
  else:
    ans+=x
print(ans)