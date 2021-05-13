N, _, C = [int(i) for i in input().split()]
B =  [int(i) for i in input().split()]
A = []
for i in range(N):
  A.append([int(i) for i in input().split()])
  
cnt = 0
for a in A:
  s = C
  for i in range(len(B)):
    s += a[i] * B[i]
  if s > 0:
    cnt += 1
    
print(cnt)