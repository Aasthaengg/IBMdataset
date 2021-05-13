import itertools
while True:
    count = 0
    n, x = map(int, raw_input().split())
    if n==0 and x==0:
        break
    #for i in xrange(1, n):
     #   for j in xrange(1, n):
      #      for k in xrange(1, n):
       #         if i!=j and  j!=k and k!=i and i+j+k==x:
    #print count
    ls = list(itertools.combinations(xrange(1, n+1), 3))
    #print ls
    l = len(ls)
    for i in xrange(l):
        if ls[i][0]+ls[i][1]+ls[i][2]==x:
            count+=1
    print count

#for x in itertools.combinations_with_replacement()