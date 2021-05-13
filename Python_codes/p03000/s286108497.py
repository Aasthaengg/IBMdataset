N,X = map(int, input().split())
L = list(map(int, input().split()))

l = []
cnt = 0
l.append(int(0))
for i in range(N):
  l.append(l[i]+L[i])
  if l[i] <= X:
    cnt += 1
if l[-1] <= X:
  cnt += 1
print(cnt)
  
