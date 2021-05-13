import math
k,m=list(map(int,input().split()))
res=m*pow(m-1,k-1)
print(res)