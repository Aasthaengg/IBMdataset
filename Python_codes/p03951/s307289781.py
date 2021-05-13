import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
s = str(input())
t = str(input())

for i in range(N):
    if s[i:]==t[:N-i]:
        break
else:
    i += 1
print(N+i)