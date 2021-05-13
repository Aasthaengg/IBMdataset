N=int(input())
s=[0]*4
for i in range(N):
  A=str(input())
  if A=='AC':
    s[0]+=1
  elif A=='WA':
    s[1]+=1
  elif A=='TLE':
    s[2]+=1
  elif A=='RE':
    s[3]+=1
print('AC','x',s[0])
print('WA','x',s[1])
print('TLE','x',s[2])
print('RE','x',s[3])
