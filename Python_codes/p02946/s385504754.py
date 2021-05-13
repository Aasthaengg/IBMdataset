k,x=[int(x) for x in input().split()]
l=list(range(x-k+1,x+k))
L=map(str,l)
print(" ".join(L))