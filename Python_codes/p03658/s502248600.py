N,K = list(map(int,input().split()))
L = list(reversed(sorted(list(map(int,input().split())))))
print(sum(L[0:K]))