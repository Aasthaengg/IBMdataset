import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    T = SI()
    ls = len(S)
    lt = len(T)
    R = []
    for i in range(ls-lt+1):
        SS = S[i:i+lt]
        is_ok = True
        for s, t in zip(SS, T):
            if s != "?" and s != t:
                is_ok = False
        if not is_ok:
            continue
        r = ""
        for j, s in enumerate(S):
            if j == i:
                r += T
            elif i < j < i+lt:
                pass
            elif s == "?":
                r += "a"
            else:
                r += s
        R.append(r)
    R.sort()
    if R:
        print(R[0])
    else:
        print("UNRESTORABLE")



if __name__ == "__main__":
    main()