K, X = map(int, input().split())

ans = [str(X+i) for i in range(-K+1, K)]
print(" ".join(ans))