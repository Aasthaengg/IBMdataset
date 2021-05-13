import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,H = MI()
X = []
for i in range(N):
    a,b = MI()
    X.append((a,0))
    X.append((b,1))

X.sort(reverse=True)

i = 0
ans = 0
while H > 0:
    x,y = X[i]
    if y == 1:
        H -= x
        i += 1
        ans += 1
    else:
        ans += (H+x-1)//x
        break

print(ans)
