import itertools
while True:
    n,x = list(map(int,input().split()))
    if n==x==0: break
    ret = 0
    for i in itertools.combinations([i+1 for i in range(n)],3):
        if sum(i) == x: ret+= 1
    print(ret)