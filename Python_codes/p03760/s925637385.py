o=input()
e=input()
ans=[]
for i in range(max(len(o),len(e))):
  try:
    ans.append(o[i])
    ans.append(e[i])
  except:
    break
print("".join(ans))