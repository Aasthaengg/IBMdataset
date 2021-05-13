import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
ans = 0
if n < 105:
    print(0)
    exit
else:
    for i in range(105, n+1, 2):
        cnt = 0
        for q in range(1,i+1):
            if i % q == 0:
                cnt += 1
        if cnt == 8:
            ans += 1
    print(ans)