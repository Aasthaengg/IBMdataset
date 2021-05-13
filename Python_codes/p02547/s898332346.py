n=int(input())
l=[]
for _ in range(n):
  s=input().split()
  l.append([int(s[0]),int(s[1])])
flag=0
for i in range(2,n):
  if l[i][0]==l[i][1] and l[i-1][0]==l[i-1][1] and l[i-2][0]==l[i-2][1]:
    flag=1
    break
if flag:
  print("Yes")
else:
  print("No")