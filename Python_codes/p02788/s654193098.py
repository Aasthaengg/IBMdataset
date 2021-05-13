import bisect

def main():
  N,D,A=map(int,input().split())
  m=sorted([int(j) for j in input().split()] for i in range(N))

  x=[m[i][0] for i in range(N)]
  es=[0]*(N+1)
  a,c=0,0
  for i in range(N):
    c-=es[i]
    if m[i][1]>A*c:
      t=(m[i][1]-A*c+A-1)//A
      a+=t
      c+=t
      es[bisect.bisect_right(x,x[i]+2*D)]+=t
  print(a)

main()