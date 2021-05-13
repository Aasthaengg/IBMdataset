import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

n,p = MI()
a = LI()
cnt = 0
for i in range(n):
    if a[i]%2 == 1:
        cnt += 1
if cnt%2 == 1:
    print(2**(n-1))
elif cnt == 0:
    if p == 1:
        print(0)
    else:
        print(2**n)
else:
    print(2**(n-1))
