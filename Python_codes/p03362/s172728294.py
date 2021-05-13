import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
s = set()
prime = []
for i in range(2, 55556):
    if i in s:
        continue
    if i%5==1:
        prime.append(i)
    cnt = 1
    while i*cnt<=55555:
        s.add(i*cnt)
        cnt += 1

print(*prime[:N])