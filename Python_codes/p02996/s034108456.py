n=int(input())
list=[list(map(int,input().split())) for _ in range(n)]
list1=sorted(list, key=lambda x:x[1])
t=0
for i in range(n):
  t+=list1[i][0]
  if not t<=list1[i][1]:
    print("No")
    break
else:
  print("Yes")
