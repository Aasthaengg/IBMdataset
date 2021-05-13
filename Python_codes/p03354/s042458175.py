import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p = tuple(p)
chk = [[set(),set()] for i in range(n)]
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True
      
par = [-1]*n
ans = 0
for i in range(m):
  x,y = [int(i) for i in input().split()]
  unite(x-1,y-1)

for i in range(n):
  m = find(i)
  chk[m][0].add(p[i])
  chk[m][1].add(i+1)

for i in range(n):
  ans += len(chk[i][0] & chk[i][1])
    
print(ans)