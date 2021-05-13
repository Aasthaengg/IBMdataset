import itertools
n = int(input())
if n%2 == 0:
    print(n*(n-2)//2)
    for i,j in itertools.combinations(range(1,n+1),2):
        if i + j == n+1:continue
        print(i,j)
else:
    print(n*(n-1)//2 - n//2)
    for i,j in itertools.combinations(range(1,n+1),2):
        if i + j == n:continue
        print(i,j)
