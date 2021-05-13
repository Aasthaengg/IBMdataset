N, T = map(int,input().split())
c = []
t = []
for i in range(N):
  c_temp, t_temp = map(int,input().split())
  c.append(c_temp)
  t.append(t_temp)
  
ans = 10000
  
for i in range(N):
  if t[i] <= T:
    if c[i] < ans:
      ans = c[i]
      
if ans == 10000:
  print('TLE')
else:
  print(ans)