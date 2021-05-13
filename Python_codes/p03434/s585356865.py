import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = sorted(list(mapint()), reverse=True)

alice = 0
bob = 0
for i in range(N):
    if i%2==0:
        alice += As[i]
    else:
        bob += As[i]
print(alice-bob)