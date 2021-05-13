K, X = map(int, input().split())
print(*list(x for x in range(max(X-(K-1),-1000000),min(X+(K-1)+1,1000000))))
