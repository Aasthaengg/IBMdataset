import sys
input = sys.stdin.readline
N,M=map(int,input().split())
lst=[0]*M
for i in range(M):
 a,b=map(int,input().split())
 c=set(map(int,input().split()))
 d=0
 for n in c:
  d+=2**(n-1)
  lst[i]=(a,d)
ans=[[float("inf") for e in range(2**N)] for f in range(M+1)]
ans[0][0]=0
for j in range(M):
 for i in range(2**N):
  e= i-(lst[j][1]&i)
  ans[j+1][i]=min(ans[j][e]+lst[j][0],ans[j][i])
if ans[M][2**N-1]==float("inf"):
 print(-1)
else:
 print(ans[M][2**N-1])