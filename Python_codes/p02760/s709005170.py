l1=[]
for i in range(3):
  a, b, c=map(int, input().split())
  l1.append(a)
  l1.append(b)
  l1.append(c)
n=int(input())

for i in range(n):
  d=int(input())
  for j in range(9):
    if l1[j]==d:
      l1[j]=0
if l1[0]+l1[1]+l1[2]==0 or l1[3]+l1[4]+l1[5]==0 or l1[6]+l1[7]+l1[8]==0 or l1[0]+l1[4]+l1[8]==0 or l1[2]+l1[4]+l1[6]==0 or l1[0]+l1[3]+l1[6]==0 or l1[1]+l1[4]+l1[7]==0 or l1[2]+l1[5]+l1[8]==0:
  print("Yes")
else:
  print("No")
