from math import ceil
N,X,T = list(map(int,input().split(' ')))

print(T*(ceil(N/X)))
