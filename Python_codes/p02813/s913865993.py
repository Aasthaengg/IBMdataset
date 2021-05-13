import sys
import math
import itertools
import collections

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    P = tuple(NLI())
    Q = tuple(NLI())
    
    ls = [x for x in range(1,N+1)]        

    p_list = list(itertools.permutations(ls))
    
    a,b = 0,0
    for x in range(len(p_list)):
        if P == p_list[x]:
            a = x
        if Q == p_list[x]:
            b = x
    print(abs(a-b))


if __name__ == '__main__':
    main()