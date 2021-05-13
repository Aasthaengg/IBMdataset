K, X = map(int, input().split())

if K == 1:
    print(X)
else:
    ans = list(range(X-(K-1), X+K))
    print(" ".join(map(str,ans)))