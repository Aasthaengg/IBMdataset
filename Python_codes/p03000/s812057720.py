N,X = map(int,input().split())
L = list(map(int,input().split()))
D = 0
a = 1

for n in range(N):
  D+=L[n]
  if D<=X:
    a+=1

print(a)