A=[]
for i in range(3):
  A.append(list(map(int, input().split())))
N = int(input())
b = []
for i in range(N):
  b.append(int(input()))
  
flugs = [[False] * 3 for i in range(3)]
for i in range(3):
  for j in range(3):
    if A[i][j] in b:
      flugs[i][j] = True
      
result = 'No'
for i in range(3):
  if all(flugs[i][:]) or all([row[i] for row in flugs]):
    result = 'Yes'
  
if all([flugs[0][0], flugs[1][1], flugs[2][2]]):
  result = 'Yes'
    
elif all([flugs[2][0], flugs[1][1], flugs[0][2]]):
  result = 'Yes'
    
print(result)