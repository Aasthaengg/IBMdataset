#<B>
K, X = map(int, input().split())
ans = [i for i in range(X - K + 1,X)]
ans += [i for i in range(X, X + K)]
print(" ".join(map(str, ans)))
