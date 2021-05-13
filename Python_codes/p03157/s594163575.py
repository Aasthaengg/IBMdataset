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
  h,w=LI()
  field=[S() for _ in range(h)]

  ans=0
  visited=[[False]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if visited[i][j]:
        continue
      if field[i][j]!='#':
        continue
      q=collections.deque()
      q.append((i,j))
      b=0
      wh=0
      while q:
        y,x=q.popleft()
        if visited[y][x]:
          continue
        if field[y][x]=='#':
          b+=1
        else:
          wh+=1
        visited[y][x]=True
        for dy,dx in dd:
          ny=y+dy
          nx=x+dx
          if not (0<=ny<h and 0<=nx<w):
            continue
          if field[y][x]==field[ny][nx]:
            continue
          if visited[ny][nx]:
            continue
          q.append((ny,nx))
      ans+=b*wh
      # print(i,j,b,wh,ans)
  return ans

# main()
print(main())
