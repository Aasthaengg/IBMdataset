import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

ss=[SI() for _ in range(3)]
ii=[0,0,0]
t=0
while 1:
    if ii[t]==len(ss[t]):
        print("ABC"[t])
        break
    nt="abc".index(ss[t][ii[t]])
    ii[t]+=1
    t=nt
