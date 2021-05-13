def main():
  import sys
  import numpy as np
  from scipy.sparse import csr_matrix
  from scipy.sparse.csgraph import floyd_warshall
  t=np.fromstring(sys.stdin.buffer.read(),'i',sep=' ')
  n,m,l=t[:3]
  t=t[3:]
  m*=3
  print('\n'.join(map(str,map(int,floyd_warshall(floyd_warshall(csr_matrix((t[2:m:3],(t[:m:3],t[1:m:3])),[n+1]*2),0)<=l)[t[m+1::2],t[m+2::2]].clip(0,n)%n-1))))
main()