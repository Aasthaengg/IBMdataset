N = int(input())
D = []
for i in range(N):
  d = int(input())
  D.append(d)
  
ans = len(set(D))
print(ans)