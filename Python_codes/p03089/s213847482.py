N = int(input())
b = list(map(int,input().split()))
l = [0]*N
for i in range(N):
  for j in range(min(N,len(b))-1,-1,-1):
    if b[j] == j+1:
      b.pop(j)
      l[i] = j+1
      break
if b == []:
  l.reverse()
  for k in range(N):
    print(l[k])
else:
  print(-1)
