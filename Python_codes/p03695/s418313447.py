import collections as c
input();a=c.Counter(i//400 for i in [*map(int,input().split())])
b,c=len(set([i for i in a.keys()if i<8])),sum([j for i,j in a.items()if i>=8])
print([b,1][b==0],b+c)