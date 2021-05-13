import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()

divisor = []
for i in range(1,int(N**.5)+1):
    if N % i == 0:
        divisor.append(i)
        if i != N//i:
            divisor.append(N//i)

ans = 0
for d in divisor:
    m = d-1
    if N//d < m:
        ans += m

print(ans)
