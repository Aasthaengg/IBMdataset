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
    cnt=[0]*5
    for _ in range(3):
        a,b=MI()
        cnt[a]+=1
        cnt[b]+=1
    for c in cnt:
        if c>2:
            print("NO")
            exit()
    print("YES")

main()