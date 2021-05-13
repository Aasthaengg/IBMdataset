N,T=map(int,input().split())
nm=1000000
for i in range(N):
  c,t=map(int,input().split())
  if nm>c and T>=t:
    nm=c
if nm==1000000:
  print("TLE")
else:
  print(nm)
