N = int(input())
Ts = list(map(int,input().split()))
M = int(input())
Ps =[list(map(int,input().split())) for i in range(M)]
s = sum(Ts)
for i in range(M):
  index = Ps[i][0]-1
  diff = Ps[i][1] - Ts[index]
  print(s+diff)
  
