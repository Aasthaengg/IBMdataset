#!/usr/bin/env python3

from collections import defaultdict


def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    N, M = MII()

    d = defaultdict(int)

    py = []
    for i in range(M):
        P, Y = MII()
        py.append((i, P, Y))
    py = sorted(py, key=lambda x: x[2])
    

    ans = [''] * M
    for i, j, k in py:
        d[j] += 1
        ans[i] = f'{j:06d}{d[j]:06d}'
    
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
