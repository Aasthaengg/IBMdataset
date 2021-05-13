n,m = map(int,input().split())
ab = [0]*n
cd = [0]*m

for i in range(n):
  ab[i] = input().split()
  
for i in range(m):
  cd[i] = input().split()
  
for i in range(n):
  tmp = []
  for j in range(m):
    tmp.append(abs (int(ab[i][0]) - int(cd[j][0])) + abs(int(ab[i][1]) - int(cd[j][1])))
  x = min(tmp) 
  ans = tmp.index(x)
  print(ans+1)