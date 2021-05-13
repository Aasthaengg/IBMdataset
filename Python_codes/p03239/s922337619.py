MIN = 100000

N,T = map(int,input().split())

for _ in range(N):
  c,t = map(int,input().split())
  if t<=T:
    MIN = min(MIN,c)
    
if MIN == 100000:
  print("TLE")
else:
  print(MIN) 