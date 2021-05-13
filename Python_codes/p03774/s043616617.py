N,M=map(int,input().split())
students,checks=[],[]
for _ in range(N):
  students.append(list(map(int,input().split())))
  pass
for _ in range(M):
  checks.append(list(map(int,input().split())))
  pass

for i in range(N):
  closed_manhattan=10**16
  closed_j=0
  for j in range(M):
    x=abs(students[i][0]-checks[j][0])
    y=abs(students[i][1]-checks[j][1])
    manhattan=x+y
    if closed_manhattan > manhattan:
      closed_manhattan=manhattan
      closed_j=j+1
  print(closed_j)

