import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
n, x = map(int, input().split())
#s = input()
#s,t = input().split()
#
readline = sys.stdin.readline
l = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

ans = 1
height = 0
for i in range(n):
    height += l[i]
    if height <= x:
        ans += 1
    else:
        break
print(ans)