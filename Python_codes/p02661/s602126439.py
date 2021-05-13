N = int(input())
As = []
Bs = []

for _ in range(N):
  a,b = map(int,input().split())
  As.append(a)
  Bs.append(b)
  
As.sort()
Bs.sort()

if N%2 == 1:
  ma = As[N//2]
  mb = Bs[N//2]
  print(mb-ma+1)
else:
  ma = (As[N//2-1] + As[N//2])/2
  mb = (Bs[N//2-1] + Bs[N//2])/2
  print(int((mb-ma)*2)+1)