import heapq

def main():
  X,Y,Z,K=map(int,input().split())
  A=list(reversed(sorted(map(int,input().split()))))
  B=list(reversed(sorted(map(int,input().split()))))
  C=list(reversed(sorted(map(int,input().split()))))
  q=[(-A[0]-B[0]-C[0],0,0,0)]
  queued={(0,0,0)}
  for i in range(K):
    v,s,t,u=heapq.heappop(q)
    print(-v)
    for e,f,g in [(s,t,u+1),(s,t+1,u),(s+1,t,u)]:
      if e>=X or f>=Y or g>=Z:
        continue
      if (e,f,g) in queued:
        continue
      heapq.heappush(q,(-(A[e]+B[f]+C[g]),e,f,g))
      queued.add((e,f,g))
      
if __name__=="__main__":
  main()