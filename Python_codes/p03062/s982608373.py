N,*A=map(int,open(0).read().split())
B=[abs(i) for i in A]
print(sum(B)-2*min(B)if len([i for i in A if i<0])%2 else sum(B))
