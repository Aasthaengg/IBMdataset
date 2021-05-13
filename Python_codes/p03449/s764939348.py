N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

def dfs(r, i, j, total):
  if i == 1 and j == N-1:
    r.append(total)
  
  if i < 1 and j < N-1:
    dfs(r, i+1, j, total+A[i+1][j])
    dfs(r, i, j+1, total+A[i][j+1])
  elif i < 1 and j == N-1:
    dfs(r, i+1, j, total+A[i+1][j])
  elif i == 1 and j < N-1:
    dfs(r, i, j+1, total+A[i][j+1])

i, j = [0]*2

r=[]
dfs(r, i, j, A[0][0])
print(max(r))
