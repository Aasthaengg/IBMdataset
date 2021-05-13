import itertools
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

X = list(itertools.permutations(range(1,n+1)))

a=None
b=None
for i, x in enumerate(X):
    if list(x) == p:
        a=i
        
    if list(x) == q:
        b=i
        
print(abs(a-b))  