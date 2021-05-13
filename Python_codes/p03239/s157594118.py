n,t=map(int,input().split())
li=[]
for i in range(n):
  c,tt=map(int,input().split())
  if tt>t:
    continue
  li.append(c)
if len(li)==0:
  print("TLE")
else:
  print(min(li))