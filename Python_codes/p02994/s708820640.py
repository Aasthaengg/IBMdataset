n, l = map(int, input().split())
ans = [l+i-1 for i in range(1, n+1)]
mn = min(ans, key=lambda x: abs(x))
print(sum(ans) - mn)