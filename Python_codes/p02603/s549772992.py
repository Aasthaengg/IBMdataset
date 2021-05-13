import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
money = 1000
for i in range(1, N):
    if As[i]>As[i-1]:
        money += (money//As[i-1])*(As[i]-As[i-1])
print(money)