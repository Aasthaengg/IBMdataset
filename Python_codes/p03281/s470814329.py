import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()

if N < 105:
    print(0)
    exit()

ans = 0
for i in range(105,N+1,2):
    cnt = 0
    for q in range(1,int(i**0.5)+1):
        if i % q == 0:
            cnt += 2
    if cnt == 8:
        ans += 1
print(ans)

