from collections import*
n,*A=map(int,open(0).read().split());C=Counter(A).items();f=1;l=len(C)
if l==3:
  x=0
  for c in C:x^=c[0]
  f=(len(set(c[1]for c in C))>1)+n%3+x>0
elif l==2:f=(abs(sum(c[1]*(-1)**i for i,c in enumerate(C)))!=n//3)+n%3>0
else:f=(l!=1)+A[0]>0
print('YNeos'[f::2])