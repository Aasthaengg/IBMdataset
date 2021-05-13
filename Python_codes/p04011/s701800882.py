from sys import stdin

def S(): return stdin.readline().rstrip()
def I(): return int(stdin.readline().rstrip())
def LS(): return list(stdin.readline().rstrip().split())
def LI(): return list(map(int,stdin.readline().rstrip().split()))

n,k,x,y=[I() for i in range(4)]

ans = 0
for i in range(n):
    if i<k:
        ans += x
    else:
        ans += y
print(ans)