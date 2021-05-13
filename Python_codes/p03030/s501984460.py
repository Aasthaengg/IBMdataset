n=int(input())
rest=[]
for i in range(n):
  s,a=map(str,input().split())
  rest.append([s,-int(a),i+1])
rest=sorted(rest, key=lambda student: (student[0],student[1]))
for i in range(n):
  print(rest[i][2])