import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
x = M*1900+(N-M)*100
ans = x*(2**M)
print(int(ans))