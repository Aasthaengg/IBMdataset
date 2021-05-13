import numpy as N;p=print;i=int;n=i(input());c=i(N.sqrt(n*2))
if c*c+c-n*2:p('No')
else:a=N.eye(c+1,c,0,i);t=N.triu_indices(c);a[t]=a[1:].T[t]=N.arange(n)+1;p('Yes');p(c+1);[p(c,*r)for r in a]