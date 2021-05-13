n, a, b = map(int, input().split())
m = a*(n-1)+b
M = a+(n-1)*b
ans = max(M-m+1, 0)
print(ans)
