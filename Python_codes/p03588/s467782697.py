n,*L=map(int,open(0).read().split());print(sum(sorted((i,j)for i,j in zip(*[iter(L)]*2))[-1]))