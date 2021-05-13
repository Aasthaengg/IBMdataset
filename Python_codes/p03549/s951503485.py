N,M = map(int,input().split())
ans = 0
ans += 1900*M
ans += 100*(N-M)
ans *= 2**M
print(ans)