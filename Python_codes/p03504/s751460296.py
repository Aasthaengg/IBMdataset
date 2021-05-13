N,C = map(int,input().split())
ST = []
for _ in range(N):
  s,t,c = map(int,input().split())
  ST.append([s,0,c])
  ST.append([t,1,c])
ST.sort(key=lambda x:x[0])
ST.sort(key=lambda x:x[2])
for i in range(len(ST)-1):
  if ST[i][2]==ST[i+1][2] and ST[i][0]==ST[i+1][0]:
    ST[i][1]=2
    ST[i+1][1]=2

ST.sort(key=lambda x:x[1])
ST.sort(key=lambda x:x[0])

ans =[0]
for st in ST:
  if st[1]==0:
    ans.append(ans[-1]+1)
  elif st[1]==1:
    ans.append(ans[-1]-1)
print(max(ans))

