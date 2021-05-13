import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A = int(input())
B = int(input())
if A>B:
    print('GREATER')
elif A<B:
    print('LESS')
else:
    print('EQUAL')