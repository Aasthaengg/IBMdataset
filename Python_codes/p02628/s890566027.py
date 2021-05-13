N, K = map(int, input().split())
P = [int(x) for x in input().split()]
P.sort()
print(sum(P[0:K]))
