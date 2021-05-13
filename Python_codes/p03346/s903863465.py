N = int(input())
ls = [0]*(N+1)
for i in range(N):
  p = int(input())
  ls[p] = i
ID = -1
count = 0
ans = 0
for a in range(1,N):
  if ls[a+1]>ls[a]:
    count += 1
  else:
    if count>ans:
      ans = count
    count = 0
if count>ans:
  ans = count
print(N-ans-1)