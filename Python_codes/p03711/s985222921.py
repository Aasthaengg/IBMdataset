a,b=map(int,input().split())
n=[1,3,5,7,8,10,12]
m=[4,6,9,11]
o=[2]
p=[n,m,o]
if (a in n and b in n) or (a in m and b in m) or (a in o and b in o):
  print('Yes')
else:
  print('No')