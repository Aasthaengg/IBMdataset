N,M = map(int,input().split())
array = list(map(int,input().split()))
task = sum(array)
if N >= task:
  print(N-task)
else:
  print(-1)