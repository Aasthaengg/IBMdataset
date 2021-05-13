import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, C, D = map(int, list(input()))

for i in ('+', '-'):
    for j in ('+', '-'):
        for k in ('+', '-'):
            val = A
            if i=='+':
                val += B
            else:
                val -= B

            if j=='+':
                val += C
            else:
                val -= C

            if k=='+':
                val += D
            else:
                val -= D
            
            if val==7:
                print('{}{}{}{}{}{}{}=7'.format(A, i, B, j, C, k, D))
                exit()