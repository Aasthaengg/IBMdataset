import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
x, a = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

if x < a:
    print(0)
else:
    print(10)