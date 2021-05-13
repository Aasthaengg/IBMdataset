n=int(input())
t=[]
for i in range(n):
  at,bt=map(int,input().split())
  t.append([bt,at])
t.sort()
temp=0
for i in range(n):
  temp=temp+t[i][1]
  if temp>t[i][0]:
    print("No")
    break
else:
  print("Yes")