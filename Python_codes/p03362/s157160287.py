import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Elastotenes's sieve -- START --
def elastotenesSieve(n):
  l1=list(range(2,n+1))
  l2=[]
  
  while True:
    if len(l1)==0:
      return l2
  
    n=l1[0]
    l2.append(n)
    for y in l1:
      if y%n==0:
        l1.remove(y)
# Elastotenes's sieve --- END ---

def main():
  n=I()
  l=elastotenesSieve(55555)

  ans=[]
  cnt=0
  for x in l:
    if x%5==1:
      ans.append(x)   
      cnt+=1

    if cnt==n:
      break

  return ' '.join([str(x) for x in ans])

# main()
print(main())
