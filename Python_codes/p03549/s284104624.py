n,m = map(int, input().split())
a = 2**m
b = 1900*m + 100*(n-m)
ans = b*(2**m)
print(ans)
