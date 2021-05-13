n=input()

l=len(n)
if int(n)>9:
  ans=[9]
else:
  print(int(n))
  exit()
tmp=n[l-1]
for i in range(2,l+1):
  #print(tmp, int(n[l-i]))
  if int(tmp) != 9:
    tmp=int(n[l-i])-1
    #print("tmp:",tmp)
  else:
    tmp=int(n[l-i])
  if i==l:
    ans.append(int(tmp))
  else:
    ans.append(9)
  #print(ans)
print(sum(ans))