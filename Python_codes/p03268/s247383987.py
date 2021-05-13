import sys

N, K = map(int, sys.stdin.readline().split())

ans = (N//K)**3

if K%2 == 0:
  ans += ((N+K//2)//K)**3
  
print(ans)