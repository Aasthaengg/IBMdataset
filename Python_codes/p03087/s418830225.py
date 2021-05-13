from sys import stdin
import numpy as np
N, Q=map(int,input().split())
S=input()
L =[list(map(int, stdin.readline().split())) for _ in range(Q)]
c = [0]*(N)  #ACのチェック
s = [0]*(N)  #ACの累積和
ans = [0]*Q 

for i in range(N-1):
  if S[i] == "A" and S[i+1] == "C":
    c[i+1] = 1
s = np.cumsum(c)
for i in range(Q):
  ans[i] = s[L[i][1]-1]-s[L[i][0]-1]

for i in ans:
  print(i)
