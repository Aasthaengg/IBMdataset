N = int(input())
A = []
for i in range(N):
  temp = int(input())
  A.append(temp)
if A[0] != 0:
  print(-1)
  exit()
ans = 0
prev = 0

for i in range(1,N+1):
  #print(prev,A[-i],ans)
  if A[-i] > N-i:
    print(-1)
    exit()
  if prev == 0:
    prev = A[-i]
    ans += A[-i]
  else:
    if A[-i] == prev-1:
      prev = A[-i]
    elif A[-i] > prev-1:
      prev = A[-i] #- (prev-1)
      ans += prev
    else:
      print(-1)
      exit()
print(ans)
