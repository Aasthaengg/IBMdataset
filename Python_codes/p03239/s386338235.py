n,t = map(int,input().split())

ct = [0]*n

for i in range(0,n):
  ct[i] = input().split()
  
s = []
for i in range(0,n):
  if(int(ct[i][1]) <= t):
    s.append(int(ct[i][0]))
if(len(s) != 0):
  print(min(s))
else:
  print("TLE")