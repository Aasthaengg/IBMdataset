n,m=map(int,input().split())
p=[0 for i in range(n)]
penalty=[0 for i in range(n)]
acc=0
for i in range(m):
  a,b=input().split()
  a=int(a)
  a-=1

  if (p[a]==0 or p[a]=='WA') and b=='AC':
    acc+=1
    p[a]='AC'
  elif (p[a]==0 or p[a]=='WA') and b=='WA':
    penalty[a]+=1
    p[a]='WA'

for i in range(n):
  if p[i] == 'WA' or p[i] == 0:
    penalty[i]=0

print(acc,sum(penalty))