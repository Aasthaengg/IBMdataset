import sys
import heapq
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

K = I()

q = K//50
p = K%50

ans = [i+q for i in range(50)]
left = 50-p
for i in range(left,50):
  ans[i] += 1

print(50)
print(" ".join(map(str, ans)))