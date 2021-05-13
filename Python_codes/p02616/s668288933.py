import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    pos = []
    neg = []
    for a in aa:
        if a < 0: neg.append(a)
        else: pos.append(a)
    pn = len(pos)
    nn = len(neg)
    if min(k,nn) // 2 * 2 + pn < k:
        aa.sort(key=lambda x: abs(x))
        print(cal(aa[:k]))
    else:
        pos.sort()
        neg.sort(reverse=True)
        ans = pos.pop() if k & 1 else 1
        mul = []
        while len(pos) > 1: mul.append(pos.pop() * pos.pop())
        while len(neg) > 1: mul.append(neg.pop() * neg.pop())
        mul.sort(reverse=True)
        print(ans * cal(mul[:k // 2]) % md)

def cal(xx):
    res=1
    for x in xx:
        res=res*x%md
    return res

md=10**9+7
n,k=MI()
aa=LI()
main()