s=list(input())
t=list(input())
ans=[]
for i in range(len(s)-len(t)+1):
  cnt=0
  for j in range(i,len(t)+i):
    if s[j]!=t[j-i]:
      cnt+=1
  ans.append(cnt)
print(min(ans))
