import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def pr(g):
    string = ''
    for row in g:
        string += ''.join([str(x) for x in row])
        string += '\n'
    print(string)

A, B = LI()
def main():
    rev = False
    global A, B
    if A < B:
        A, B = B, A
        rev = True
    h = 100
    w = 100
    g = [[0 for _ in range(w)] for __ in range(h)]
    cnt = 0

    def fill(i=None, j=None):
        global A, B
        filled = False
        if i:
            st = i
        else:
            st = 0
        if j:
            stj = j
        else:
            stj = 0
        # l_i, l_j = 0, 0
        for i in range(st+1, h-1):
            if filled:
                break
            for j in range(w-1):
                if A == 0:
                    filled = True
                    l_i, l_j = i, j
                    break
                if i % 2 == 1 and j % 2 == 1:
                    g[i][j] = 1
                    A -= 1
        return l_i, l_j

    last_i, last_j = fill()

    def fill_left_up(i, j):
        cp_i = i
        if i-1 >= 0:
            while g[i-1][j] == 0:
                g[i-1][j] = 1
                i -= 1
                if i-1 < 0:
                    break
        i = cp_i
        if j-1 >= 0:
            while g[i][j-1] == 0:
                g[i][j-1] = 1
                j -= 1
                if j-1 < 0:
                    break

    first = True
    B -= 1
    for i in range(h-1):
        for j in range(w-1):
            if g[i][j] == 1 and B > 0:
                fill_left_up(i, j)
                B -= 1
                if first:
                    first = False
                else:
                    A += 1

    fill(last_i, last_j)

    A_symbol = '.'
    B_symbol = '#'
    if rev:
        A_symbol, B_symbol = B_symbol, A_symbol
    print(h, w)
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                print(A_symbol, end='')
            else:
                print(B_symbol, end='')
        print()



main()


