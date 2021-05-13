import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
p, q, r = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

ans = min([p+q, p+r, q+r])

print(ans)