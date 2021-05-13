A,B=map(int,input().split())
c=min([(A+B)%3,A%3,B%3])
print(['Possible','Impossible'][c!=0])