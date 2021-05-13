n,k=map(int,input().split())
from itertools import*
print(n-max(len(list(groupby(input())))-k*2,1))