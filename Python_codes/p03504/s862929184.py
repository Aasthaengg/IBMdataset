N,C=map(int,input().split())
ch=[[] for i in range(31)]
for i in range(N):
  s,t,c=map(int,input().split())
  ch[c].append([s,t])
arr=[[] for i in range(31)]
start=[]
end=[]
for i in range(31):
  score=[0]*(10**5+1)
  for j in range(len(ch[i])):
    score[ch[i][j][0]]+=1
    score[ch[i][j][1]]-=1
  for j in range(10**5+1):
    if score[j]==1:
      start.append(j)
    if score[j]==-1:
      end.append(j)
ans=[0]*(10**5+3)
for i in start:
  ans[i]+=1
for j in end:
  ans[j+1]-=1
for i in range(10**5):
  ans[i+1]+=ans[i]
print(max(ans))
