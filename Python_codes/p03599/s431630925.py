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
  A,B,C,D,E,F=LI()
  ans_pair=[0,0]
  ans_noudo=0
  for a in range(31):
    for b in range(31):
      for c in range(3001):
        for d in range(3001):

          sato=c*C+d*D
          mizu=100*A*a+100*B*b
          satomizu=sato+mizu
          # if satomizu==2634 and sato==934:
          #   print(satomizu,sato)

          if satomizu==0:
            continue

          if F<satomizu:
            break

          noudo=(100*sato)/(satomizu)
          E_noudo=(100*E)/(100+E)
          if E_noudo<noudo:
            break

          if ans_noudo<=noudo:
            ans_noudo=noudo
            ans_pair=[satomizu,sato]
            # print(noudo,satomizu,sato,mizu,a,b,c,d)

  return str(ans_pair[0])+' '+str(ans_pair[1])

# main()
print(main())
