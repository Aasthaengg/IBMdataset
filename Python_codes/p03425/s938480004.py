import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    S = [SS() for _ in range(N)]

    cnt = collections.Counter([i[0] for i in S])
    # print(cnt)
    ans = 0
    for i, j, k in itertools.combinations(('M', 'A', 'R', 'C', 'H'), 3):
        ans += cnt[i] * cnt[j] * cnt[k]

    print(ans)

if __name__ == '__main__':
    resolve()
