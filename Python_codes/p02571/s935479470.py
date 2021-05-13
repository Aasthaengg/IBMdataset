s=list(input())
t=list(input())
ans=[]
for i in range(len(s)-len(t)+1):
  ct=0
  for j in range(len(t)):
    if s[i+j]!=t[j]:
      ct+=1
  ans.append(ct)
print(min(ans))