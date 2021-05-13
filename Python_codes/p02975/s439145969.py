import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15
from collections import deque,defaultdict,Counter

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if N%3 == 0:
        C = Counter(A)
        flag = True
        if len(C) > 3:
            flag = False
        elif len(C) == 3:
            a,b,c = tuple(C.keys())
            for _ in range(3):
                if a^b == c:
                    a,b,c = b,c,a
                else:
                    flag = False
                    break
            if not all(v*3 == N for v in C.values()):
                flag = False
        elif len(C) == 2:
            a,b = tuple(C.keys())
            if a*b == 0:
                if C[0]*3 == N:
                    pass
                else:
                    flag = False
            else:
                flag = False
        else:
            if 0 not in C:
                flag = False
        print('Yes' if flag else 'No')
    else:
        if set(A) == {0}:
            print('Yes')
        else:
            print('No')
if __name__ == '__main__':
    main()