N,T = map(int,input().split())
A = []

for n in range(N):
  c,t = map(int,input().split())
  if t<=T:
    A.append(c)

if len(A)==0:
  print("TLE")
else:
  print(min(A))