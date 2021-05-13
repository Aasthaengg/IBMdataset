n,k=map(int,open(0));p=1
for _ in range(1,n+1):p=[p+k,p*2][p*2<p+k]
print(p)