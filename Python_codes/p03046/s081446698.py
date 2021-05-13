import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    M, K = map(int, line_input())
    if K >= pow(2, M): print(-1)
    elif M == 0:
        if K == 0: print("0 0")
        else: print(-1)
    elif M == 1:
        if K == 0: print("0 0 1 1")
        else: print(-1)
    else:
        ans = []
        if K == 0: ans = [int(i)//2 for i in range(2 ** (M + 1))]
        else:
            ans.append(K)
            for i in range(2 ** M):
                if i != K: ans.append(i)
            ans.append(K)
            for i in reversed(range(2 ** M)):
                if i != K: ans.append(i)
        print(" ".join(map(str, ans)))
    return 0
  
if __name__ == "__main__":
    solve()