n = int(input())

LR = [list(map(int, input().split())) for i in range(n)]

j = 0
for i in range(n):
  j += (LR[i][1]-LR[i][0] + 1)
  
print(j)