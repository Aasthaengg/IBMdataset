n = int(input())
lr = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0

for i in range(n):
  ans += (lr[i][1] - lr[i][0]) +1
  
  
print(ans)

