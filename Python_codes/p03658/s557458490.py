N,K,*L = map(int,open(0).read().split())
L.sort(reverse=True)
print(sum(L[:K]))