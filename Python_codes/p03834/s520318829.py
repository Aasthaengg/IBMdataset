s=input()
ans=[]
for i in str(s):
  if i==",":
    ans.append(" ")
  else:
    ans.append(i)
a="".join(ans)
print(a)