K,X = (int(x) for x in input().split())
print(' '.join(map(str,list(range(X-K+1,X+K)))))