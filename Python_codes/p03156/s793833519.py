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
    n=II()
    a,b=MI()
    pp=MI()
    cnt=[0]*3
    for p in pp:
        if p>b:cnt[0]+=1
        elif p>a:cnt[1]+=1
        else:cnt[2]+=1
    print(min(cnt))

main()