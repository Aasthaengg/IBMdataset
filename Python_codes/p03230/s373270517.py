import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()
  k=2
  while True:
    kk=k*(k-1)
    if kk>n*2:
      print('No')
      exit()
    if kk==n*2:
      break
    k+=1

  print('Yes')
  print(k)
  ans=[[] for _ in range(k)]
  ln=2*n//k

  st=0
  for i in range(k):
    tmp=[]
    i_ln=ln-len(ans[i])
    for j in range(i_ln):
      st+=1
      tmp.append(st)
    ans[i]+=tmp
    
    for j in range(i+1,k):
      ans[j].append(tmp.pop())

  # print(ans)
  for x in ans:
    print(ln,' '.join(str(y) for y in x))

main()
# print(main())
