import sys
import heapq

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
mo = 10**9+7

def main():
    N = II()
    A = LI()
    A.sort(reverse=True)
    ans = 0
    hq=[]
    heapq.heapify(hq)
    heapq.heappush(hq,A[0]*-1)
    for i,a in enumerate(A[1:]):
        ans+=heapq.heappop(hq)*-1
        heapq.heappush(hq,a*-1)
        heapq.heappush(hq,a*-1)
    print(ans)

    

if __name__ == '__main__':
    main()