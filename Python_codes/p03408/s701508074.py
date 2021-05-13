N = int(input())
s = []
for i in range(N):
  s.append(input())
M = int(input())
t = []
for i in range(M):
  t.append(input())
  
c = list(set(s))
ans = 0
for i in range(len(c)):
  ans = max([ans, s.count(c[i])-t.count(c[i])])
  
print(ans)