N,C = map(int,input().split())
num = 100009*2
channel = [[0]*num for _ in range(C)]
time = [0]*num

max_num = 0
for i in range(N):
  s,t,c = map(int,input().split())
  s,t,c = 2*s-1,2*t,c-1
  if(channel[c][s-1] == 1): channel[c][s-1] = 0
  else: channel[c][s] = 1 
  channel[c][t] = 1
  max_num = max(max_num,t)

tmp = 0
for i in range(C):
 for j in range(max_num+15):
  if((tmp == 0)and(channel[i][j] == 1)):
    tmp = 1
    a = j
  elif((tmp == 1)and(channel[i][j] == 1)):
    tmp = 0
    b = j
    time[a] += 1
    time[b+1] -= 1

ans = 0    
for i in range(max_num+15):
  if(i != 0): time[i] += time[i-1]
  ans = max(ans,time[i])
print(ans)                         