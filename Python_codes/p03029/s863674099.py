import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
a, p = map(int, input().split())
#s = input()
#s,t = input().split()
#a = [int(input()) for _ in range(n)]
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

ans = (3*a+p)//2
print(ans)