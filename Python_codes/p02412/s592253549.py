import itertools
while True:
    n,x = [int(x) for x in input().split()]
    if (n,x)==(0,0): break
    cnt=0
    for comb in itertools.combinations(range(1,n+1),3):
        if sum(comb) == x: cnt+=1
    print(cnt)