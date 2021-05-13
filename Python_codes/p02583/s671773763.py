import itertools as it
n=int(input())
a=sorted(map(int,input().split()))
print(sum(sum(x)>2*x[2]and len(x)==len(set(x))for x in it.combinations(a,3)))