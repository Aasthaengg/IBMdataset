import sys
input = sys.stdin.readline
N,M,Q=map(int,input().split())
lst=[[0 for e in range(N+1)] for f in range(N+1)]
for i in range(M):
 L,R=map(int,input().split())
 for j in range(1,L+1):
  lst[j][R]+=1
for j in range(N):
 for i in range(N+1):
  lst[i][j+1]+=lst[i][j]
for i in range(Q):
 p,q=map(int,input().split())
 print(lst[p][q])
