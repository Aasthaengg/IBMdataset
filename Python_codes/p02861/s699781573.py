import math
N=int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
L=list()
for i in range(N-1):
  for j in range(i,N):
    L.append(((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**(1/2))
    
print(2*math.factorial(N-1)*sum(L)/math.factorial(N))