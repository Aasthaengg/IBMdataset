N,M,X = map(int,input().split())
S = list(map(int,input().split()))
path = [0 for _ in range(N+1)]
for n in S:
  path[n] = 1
  
left = sum(path[1:X])
right = sum(path[X:-1])

print(min(left,right))