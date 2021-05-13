import numpy as np
#-------------
N = int(input())
T,A = map(int, input().split())
H =list(map(int, input().split()))
#-------------
Temp = []

for i in range(N) :
  Temp.append(T-0.006*H[i]-A)
  
Temp = np.abs(Temp)
cnt =1
for i in range(N):
  if min(Temp) != Temp[i]:
    cnt+=1
  else:
    print(cnt)