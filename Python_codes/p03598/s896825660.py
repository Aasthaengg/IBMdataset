n,k,*x = map(int, open(0).read().split())
print(sum(k-i if k/2 < i else i for i in x)*2)