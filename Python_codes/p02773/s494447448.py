N = int(input())

d = dict()

for i in range(N):
  s = input()
  if s in d:
    d[s]+=1
  else:
    d[s]=1

d = sorted(d.items(), key=lambda x:-x[1])
i=0
ans=[]
while i<len(d):
  ans.append(d[i][0])
  if i<len(d)-1 and d[i+1][1]==d[i][1]:
      i+=1
  else:
    break

ans = sorted(ans)

for i in range(len(ans)):
  print(ans[i])