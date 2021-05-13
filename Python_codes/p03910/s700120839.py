n=int(input())
temp=0
i=1
ans=[]
while True:
  temp=temp+i
  ans.append(i)
  if temp>=n:
    break
  i=i+1
t=temp-n
for i in range(len(ans)):
  if ans[i]!=t:
    print(ans[i])