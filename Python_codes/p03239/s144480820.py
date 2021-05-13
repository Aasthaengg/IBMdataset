n,t=map(int,input().split())

c=[]
for i in range(n):
  c_=list(map(int,input().split()))
  c.append(c_)
  
c.sort()

for i in range(n):
  if c[i][1]<=t:
    print(c[i][0])
    exit()
    
  else:
    continue
    
print('TLE')
