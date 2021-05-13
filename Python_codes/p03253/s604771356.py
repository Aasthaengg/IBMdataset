def resolve():
    n,m= map(int, input().split())
    a=[]
    b=[]
    i=2
    l=1
    while m!=1:
      while m%i!=0:
        i+=1
      a.append(i)
      m=m//i
    au=list(set(a))
    for j in range(len(au)):
        b.append(a.count(au[j]))
    from operator import mul
    from functools import reduce

    def cmb(n, r):
        r = min(n - r, r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under

    for k in b:
        l*=cmb(k+n-1,n-1)

    print(l%(10**9+7))
resolve()