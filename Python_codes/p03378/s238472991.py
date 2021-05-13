# B - Toll Gates
N,M,X = map(int,input().split())
A = list(map(int,input().split()))
l = len([a for a in A if a<X])
print(min(l,M-l))