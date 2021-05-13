from numpy import*;p=print;i=int;n=i(input());c=i(sqrt(n*2))
if c*c+c-n*2:p('No')
else:a=eye(c+1,c,0,i);t=triu_indices(c);a[t]=a[1:].T[t]=r_[:n]+1;p('Yes');p(c+1);[p(c,*r)for r in a]