import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

a,b,k=map(int,input().split())
ans=[]
for i in range(a,min(a+k,b+1)):
  ans.append(i)
for i in range(max(b-k+1,a),b+1):
  ans.append(i)
ans = sorted(list(set(ans)))
for i in ans:
  print(i)