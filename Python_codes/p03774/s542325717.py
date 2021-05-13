
def calc(N, M, student, point) : 
  translatepoint = list()
  for i in range(N) : 
    mindistance = 10 ** 9
    minpoint = -1
    for j in range(M) : 
      distance = abs(student[i][0] - point[j][0]) + abs(student[i][1] - point[j][1])
      if distance < mindistance : 
        mindistance = distance
        minpoint = j + 1
    
    translatepoint.append(minpoint)
  return translatepoint


N, M = tuple(map(int, input().split()))
student = list()
point = list()

for i in range(N) : 
  student.append(tuple(map(int, input().split())))
  
for j in range(M) : 
  point.append(tuple(map(int, input().split())))
  
ans = calc(N, M, student, point)

for i in range(len(ans)) : 
  print(ans[i])