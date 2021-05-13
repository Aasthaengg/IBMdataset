from math import ceil,floor

N=int(input())
X=ceil(N/1.08)
print(X if floor(X*1.08)==N else ":(")
