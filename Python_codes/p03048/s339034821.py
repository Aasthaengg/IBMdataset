R, G, B, N = map(int, input().split())

A = [R,G,B]

count=0
for i in range(N+1):
  for j in range(N+1):
    if N-i*A[0]-j*A[1]<0:
      break
    elif (N-i*A[0]-j*A[1])%A[2]==0:
      count+=1

print(count)