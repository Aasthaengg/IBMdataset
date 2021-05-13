N = int(input())
P = [[0,0,0]]+[list(map(int,input().split())) for n in range(N)]
ans = "Yes"

for n in range(N):
  dt = P[n+1][0]-P[n][0]
  dx = abs(P[n+1][1]-P[n][1])
  dy = abs(P[n+1][2]-P[n][2]) 
  if dt<dx+dy or dt%2!=(dx+dy)%2:
    ans = "No"

print(ans)