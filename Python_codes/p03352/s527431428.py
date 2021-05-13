import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())

s = set([1])
for i in range(min(2, X), X):
    cnt = 2
    while i**cnt<=X:
        s.add(i**cnt)
        cnt += 1

print(max(s))