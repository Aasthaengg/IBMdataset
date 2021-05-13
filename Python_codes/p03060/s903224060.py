import sys
sys.setrecursionlimit(10**6)

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
#n, m = map(int, input().split())
#s = input()
#s,t = input().split()
#a = [int(input()) for _ in range(n)]
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

ans = 0

for i,j in zip(v,c):
    if i > j:
        ans += i-j
        
print(ans)