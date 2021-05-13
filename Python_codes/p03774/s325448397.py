n,m = map(int, input().split())
s = [tuple(map(int,input().split())) for _ in range(n)]
c = [tuple(map(int,input().split())) for _ in range(m)]
for i in range(n):
  mini = 0
  m_i = 0
  for j in range(m):
    dis = abs(s[i][0]-c[j][0])+abs(s[i][1]-c[j][1])
    if j==0:
      mini, m_i = dis, j+1
      continue
    elif mini > dis:
      mini, m_i = dis, j+1
  print(m_i)