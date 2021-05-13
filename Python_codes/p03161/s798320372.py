from numba import jit
n,k=map(int,input().split())
h=list(map(int,input().split()))
@jit
def jitcalc(n,k,h):
  cost=[0]
  for i in range(1,n):
    wk=[]
    for j in range(1,min(k,i)+1):
      wk.append(cost[i-j]+abs(h[i]-h[i-j]))
    cost.append(min(wk))
  print(cost[n-1])
jitcalc(n,k,h)