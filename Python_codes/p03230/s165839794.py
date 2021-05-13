import numpy as N;p=print;n=int(input());c=int(N.sqrt(n*2))
if c**2+c-n*2:p('No')
else:a=N.zeros((c+1,c));t=N.triu_indices(c);a[t]=a[1:].T[t]=N.arange(n)+1;p('Yes');p(c+1);[p(c,*map(int,r))for r in a]