import math
def main():
  n,time = list(map(int,input().split()))
  ct = [map(int, input().split()) for _ in range(n)]
  c,t = [list(i) for i in zip(*ct)]
  cost=1001
  for i in range(0,n):
    if t[i]<=time and c[i]<cost:
      cost=c[i]
  if cost==1001:
    print("TLE")
  else:
    print(cost)
main()