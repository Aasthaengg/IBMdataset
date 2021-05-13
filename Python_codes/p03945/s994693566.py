import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    S = list(input())

    obj = S[0]
    cnt = 1
    L = []
    for i in range(1, len(S)):
        if S[i] == obj:
            cnt += 1
        else:
            L.append(cnt)
            obj = S[i]
            cnt = 1
    L.append(cnt)

    # print(L)
    print(len(L) - 1)


if __name__ == '__main__':
    solve()
