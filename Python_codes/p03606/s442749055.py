n = int(input())
rl = [0]*n

for i in range(n):
  rl[i] = input().split()
  
ans = []

for i in range(n):
  c = 0
  c = int(rl[i][1]) - int(rl[i][0]) + 1
  ans.append(c)
  
print(sum(ans))
