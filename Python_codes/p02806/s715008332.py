N=int(input())

stlist=[]
for _ in range(N):
  s,t=input().split()
  stlist.append((s,t))
#print(stlist)

X=input()

answer=0
flg=False
for s,t in stlist:
  if s==X:
    flg=True
  else:
    if flg:
      answer+=int(t)
      
print(answer)