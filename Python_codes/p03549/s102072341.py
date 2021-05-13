N,M = map(int,input().split())
ans = (N-M) * 100
ans += M*1900
ans *= 2**M
print(ans)