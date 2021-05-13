import collections
N=int(input())
V=list(map(int,input().split()))
l=N//2
V_odd=[]
V_eve=[]
for i in range(N):
  if i%2==0:
    V_odd.append(V[i])
  else:
    V_eve.append(V[i])

p_odd = list(collections.Counter(V_odd).most_common())
p_eve = list(collections.Counter(V_eve).most_common())
p_odd.append([0,0])
p_eve.append([0,0])

if p_odd[0][0]!=p_eve[0][0]:
  print(N-p_odd[0][1]-p_eve[0][1])
else:
  print(min(N-p_odd[0][1]-p_eve[1][1],N-p_odd[1][1]-p_eve[0][1]))
