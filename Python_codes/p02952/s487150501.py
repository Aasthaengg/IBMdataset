import sys
sys.setrecursionlimit(10**6)

n = int(input())
#b = list(map(int, input().split()))
#n, m = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

l = [i for i in range(1,10)] + [i for i in range(100,1000)] + [i for i in range(10000,100000)] 

n = [i for i in range(1,n+1)]

ans = len(set(l) & set(n))

print(ans)