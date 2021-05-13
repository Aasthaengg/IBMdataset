from bisect import *
n,a,b,c=[sorted(map(int,input().split())) for _ in [0]*4]
print(sum(bisect_left(a,x)*(n[0]-bisect_right(c,x)) for x in b))