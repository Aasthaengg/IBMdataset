import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(str(input()))
length = len(S)
cnt = 0
for a, b in zip(S, S[::-1]):
    if a!=b:
        cnt += 1
print(cnt//2)