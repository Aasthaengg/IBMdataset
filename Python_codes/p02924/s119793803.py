import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
#1,2,3,...,Nまでの順列の合計
#実はN(N+1)//2で表せる
def sigma(n):
    return n*(n+1)//2

print(sigma(n-1))