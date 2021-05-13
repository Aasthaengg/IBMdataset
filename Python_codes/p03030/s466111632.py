import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
 
SP = []
for i in range(N):
  s,p = input().split()
  SP.append((s,-int(p),i+1))
  
SP.sort()
 
for s,p,i in SP:
  print(i)