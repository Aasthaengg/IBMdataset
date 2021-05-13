import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

n,c,k = MI()
t = sorted([I() for _ in range(n)])

cnt = 1
b = 1
bt = t[0]+k
for i in range(1, n):
    if cnt == c or t[i] > bt:
        b += 1
        bt = t[i]+k
        cnt = 1
    else:
        cnt += 1
print(b)
