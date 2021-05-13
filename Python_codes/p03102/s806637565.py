N,M,C = map(int,input().split())
B = list(map(int,input().split()))
a = 0

for n in range(N):
  A = list(map(int,input().split()))
  if 0<sum([a*b for a,b in zip(A,B)])+C:
    a+=1

print(a)