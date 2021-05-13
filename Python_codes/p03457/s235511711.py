import sys
N = int(input())
T = []
for _ in range(N):
	T.append(list(map(int,input().split())))

#--------------------------------------------
now = [0,0]
now_time = 0
for i in range(N):
  left_time = T[i][0] - now_time
  target = [T[i][1],T[i][2]]
  distance = abs(T[i][1]-now[0]) + abs(T[i][2]-now[1])
  if distance <= left_time and distance % 2 == left_time % 2:
    now_time = T[i][0]
    now = target
    
  else:
    print("No")
    sys.exit()

print("Yes")
