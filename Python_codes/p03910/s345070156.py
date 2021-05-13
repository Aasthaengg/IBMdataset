import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
cnt = 0
s = set()
for i in range(1, N+1):
    cnt += i
    s.add(i)
    if cnt>=N:
        break
if N!=cnt:
    s.remove(cnt-N)

for i in s:
    print(i)