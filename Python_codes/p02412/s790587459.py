import itertools
while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    else:
         s=list(range(1,n+1))
         l=list(itertools.combinations(s,3))
         c=0
         for i in l:
              if sum(i) == x:
                   c+=1
         print(c)