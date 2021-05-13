import sys
import bisect
import math
import itertools
from collections import deque
import copy

# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    L = [[] for _ in range(N + 1)]

    for j in range(N):
        a = list(map(int, input().split()))
        L[j + 1] = deque(a)


    k =0

    current_revise =set(range(N+1))
    while k<50000000: # １日分の作業

        pre_revise =copy.copy(current_revise)
        current_revise =set()

        for i in pre_revise: #一人分の作業
            if not L[i]:
                continue
            can = L[i][0]
            if L[can][0] == i and i not in current_revise and can not in current_revise:
                L[i].popleft()
                L[can].popleft()

                current_revise.add(i)
                current_revise.add(can)
        k += 1

        if len(current_revise)==0:
            break


    for i in range(N + 1):
        if len(L[i])>0:
            print(-1)
            exit()

    print(k-1)

if __name__ == "__main__":
    main()
