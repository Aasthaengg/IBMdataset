N,K = map(int, input().split())
*L, = map(int, input().split())

L.sort(reverse=True)
print(sum(L[0:K]))