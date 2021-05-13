n,m = map(int,input().split())
 
p = []
for i in range(m):
  x = str(i)+' '+input()
  p.append(list(map(int,x.split())))

p.sort(key=lambda x:x[2]) 
c = [1]*(n+1)
for i in range(m):
  p[i][2] = c[p[i][1]]
  c[p[i][1]] += 1
p.sort()
for i in range(m):
  print( str(p[i][1]).zfill(6) + str(p[i][2]).zfill(6))