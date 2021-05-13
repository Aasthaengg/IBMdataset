N,A,B,*P=map(int,open(0).read().split())
C=[0]*3
for p in P:
    C[(A<p)+(B<p)]+=1
print(min(C))