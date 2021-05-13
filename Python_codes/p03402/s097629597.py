A,B=map(int,input().split())
ans=[[] for _ in range(100)]
for i in range(100):
  for j in range(100):
    if i<50:
      ans[i].append(".")
    else:
      ans[i].append("#")
A-=1
B-=1
for i in range(0,50,2):
  for j in range(0,100,2):
    if B>0:
      ans[i][j]="#"
      B-=1
for i in range(51,100,2):
  for j in range(0,100,2):
    if A>0:
      ans[i][j]="."
      A-=1
print(100,100)
for i in range(100):
  print("".join(ans[i]))