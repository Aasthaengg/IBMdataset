import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
AB = []
for _ in range(N):
    a, b = mapint()
    AB.append((a, b))
AB.sort(key=lambda x:x[1])
now = 0
for i in range(N):
    a, b = AB[i]
    if b-a<now:
        print('No')
        break
    now += a
else:
    print('Yes')