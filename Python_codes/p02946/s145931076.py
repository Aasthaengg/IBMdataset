K, X = map(int, input().split())

L = [i for i in range(X-K+1, X+1)]
R = [i for i in range(X+1, X+K)]

print(*(L+R))