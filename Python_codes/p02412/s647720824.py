import itertools
while 1:
    n,s=map(int, input().split())
    if n==0: break
    print(len([1 for c in itertools.combinations(range(1,n+1), 3) if sum(c)==s]))