import itertools
while True:
    n,x = list(map(int,input().split()))
    if n==x==0: break
    li = list(itertools.combinations([i+1 for i in range(n)],3))
    ret = 0
    for i in range(len(li)):
        if sum(li[i]) == x: ret+= 1
    print(ret)