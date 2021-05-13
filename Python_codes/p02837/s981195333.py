import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
shogens = []

for i in range(n):
    a = I()
    shogens.append([])
    for j in range(a):
        x,y = LI()
        x -= 1
        shogens[-1].append((x,y))

def is_honest(i,j):
    return (i >> j) % 2 == 1

def honest_cnt(i):
    ans = 0
    for j in range(n):
        ans += is_honest(i,j)
    return ans 

ans = 0
for i in range(1 << n):
    ok = True
    for j in range(n):
        if not is_honest(i,j):continue
        for (x,y) in shogens[j]:
            if y == 0 and is_honest(i,x):ok = False
            if y == 1 and not is_honest(i,x):ok = False
    if ok:
        ans = max(ans, honest_cnt(i))
print(ans)