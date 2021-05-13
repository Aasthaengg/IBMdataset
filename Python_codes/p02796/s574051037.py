n = int(input())
robot = list(list(map(int, input().split(' '))) for i in range(n))

for i in range(n):
  robot[i].append(robot[i][0]-robot[i][1])
  robot[i].append(robot[i][0]+robot[i][1])

robot.sort(key=lambda x: x[3])

ans=1
left=robot[0][2]
right=robot[0][3]
for i in range(1,n):
  if robot[i][2]>=right:
    ans+=1
    right=robot[i][3]
    
    
print(ans)  