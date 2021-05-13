N, K = list(map(lambda x: int(x), input().split(" ")))
L = list(map(lambda l: int(l), input().split(" ")))
L.sort(reverse=True)
print(sum(L[0:K]))