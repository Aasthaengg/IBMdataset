import sys
import numpy as np
import scipy.sparse as ss
f=ss.csgraph.floyd_warshall
def main():
  t=np.fromstring(sys.stdin.buffer.read(),int,sep=' ')
  n,m,l=t[:3]
  m=m*3+3
  d=f(f(ss.csr_matrix((t[5:m:3],(t[3:m:3],t[4:m:3])),[n+1]*2),0)<=l)[t[m+1::2],t[m+2::2]]
  d[d>n]=0
  print('\n'.join((d.astype(int)-1).astype(str).tolist()))
main()