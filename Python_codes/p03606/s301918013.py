N = int(input())
M = [list(map(int,input().split()))for _ in range(N)]
sum = 0
for i in range(N):
  sum = sum + M[i][1]-M[i][0]+1
print(sum)