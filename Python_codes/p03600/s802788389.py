#import numpy as np
#from scipy.sparse.csgraph import floyd_warshall,csgraph_from_dense
#from scipy.sparse import csr_matrix
import sys
input = sys.stdin.readline
def inputs():return [int(x) for x in input().split()]
N= int(input())
dist_mat=[inputs() for _ in range(N)]
ans=0
for i in range(N):
  for j in range(N):
    for k in range(N):
      if dist_mat[j][k]==dist_mat[j][i]+dist_mat[i][k] and dist_mat[j][i]>0 and dist_mat[i][k]>0:
        #ans+=dist_mat[j][k]
        dist_mat[j][k]=0
      elif dist_mat[j][k]>dist_mat[j][i]+dist_mat[i][k] and dist_mat[j][i]>0 and dist_mat[i][k]>0:
        print(-1)
        exit()
for i in range(N):
  for j in range(N):
    ans +=dist_mat[i][j]
print(ans//2)
#print(ans//2)

