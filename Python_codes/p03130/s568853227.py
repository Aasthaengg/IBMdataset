import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n=4
es=[[] for i in range(n)]
for i in range(n-1):
   a,b=map(int,input().split())
   es[a-1].append(b-1)
   es[b-1].append(a-1)
use=sorted([len(es[i]) for i in range(4)])

print("YES" if use==[1,1,2,2] else "NO")