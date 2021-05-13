N=int(input())
ans=[0,0,0,0]
judge=['AC','WA','TLE','RE']
for i in range(N):
  S=input()
  for j in range(4):
    if S==judge[j]:
      ans[j]+=1
      break

for i in range(4):
  print('{} x {}'.format(judge[i],ans[i]))