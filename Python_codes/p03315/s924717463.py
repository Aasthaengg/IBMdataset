import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = input()
ans = S.count('+')-S.count('-')
print(ans)