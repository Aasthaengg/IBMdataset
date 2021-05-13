from collections import deque, defaultdict

def main():
  n=int(input())
  edges=[tuple(map(int,input().split())) for _ in range(n-1)]
  d=defaultdict(list)
  for e in edges:
    d[e[0]].append(e[1])
    d[e[1]].append(e[0])
  def dist(m):
    c=-1
    dl=[-1]*(n+1)
    cv=deque([m])
    nv=deque([1])
    while nv:
      c+=1
      cv.extend(nv)
      nv.clear()
      for e in cv:
        dl[e]=c
        for x in d[e]:
          if dl[x]<0:
            nv.append(x)
      cv.clear()
    return dl[1:]
  fnc=dist(1)
  snk=dist(n)
  j=sum([(fnc[i]<=snk[i])-(fnc[i]>snk[i]) for i in range(n)])
  if j>0:
    print('Fennec')
  else:
    print('Snuke')

if __name__=='__main__':
    main()
