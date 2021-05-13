n,m = map(int,input().split())
A = list(map(int,input().split()))

for a in A:
    n-=a
if n<0:
    n=-1 
print( n )
