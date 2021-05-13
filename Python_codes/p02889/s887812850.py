import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall as f
def main():
  t=np.fromfile(open(0,'rb'),'i',sep=' ')
  n,m,l=t[:3]
  m=m*3+3
  print('\n'.join((f(f(csr_matrix((t[5:m:3],(t[3:m:3],t[4:m:3])),[n+1]*2),0)<=l)[t[m+1::2],t[m+2::2]].clip(0,n).astype(int)%n-1).astype(str).tolist()))
main()