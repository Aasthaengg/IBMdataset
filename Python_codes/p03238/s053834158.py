import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
if N==1:
    print('Hello World')
else:
    A = int(input())
    B = int(input())
    print(A+B)