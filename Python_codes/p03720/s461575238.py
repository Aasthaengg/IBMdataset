N,M = map(int,input().split())
vec = [0]*N
for i in range(M):
  A,B = map(int,input().split())
  vec[A-1] += 1
  vec[B-1] += 1
for j in range(N):
  print(vec[j])