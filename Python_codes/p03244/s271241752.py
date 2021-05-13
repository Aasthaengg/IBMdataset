n=int(input())
V=list(map(int,input().split()))

A=[V[i] for i in range(0,n,2)]
B=[V[i] for i in range(1,n,2)]

import collections
  
C = collections.Counter(A)
D = collections.Counter(B)
  
if C.most_common()[0][0] != D.most_common()[0][0]:
  print(len(A)+len(B)-C.most_common()[0][1]-D.most_common()[0][1])
else:
  if len(C)!=1 and len(D)!=1:
    print( min(len(A)+len(B)-C.most_common()[0][1]-D.most_common()[1][1],
            len(A)+len(B)-C.most_common()[1][1]-D.most_common()[0][1]) )
  elif len(C)!=1 and len(D)==1:
    print( min(len(A)+len(B)-C.most_common()[0][1]-D.most_common()[0][1],
            len(A)+len(B)-C.most_common()[1][1]-D.most_common()[0][1]) )
  elif len(C)==1 and len(D)!=1:
    print( min(len(A)+len(B)-C.most_common()[0][1]-D.most_common()[1][1],
            len(A)+len(B)-C.most_common()[0][1]-D.most_common()[0][1]) )
  else:
    print(min(len(A),len(B)))