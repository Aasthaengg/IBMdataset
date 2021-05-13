k,x = map(int,input().split())
print(" ".join([str(n) for n in list(range(x-k+1,x+k))]))