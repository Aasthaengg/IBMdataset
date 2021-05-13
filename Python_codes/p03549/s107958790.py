n,m = map(int,input().split())

ans = 0

ans += m * 1900
ans += (n-m) * 100

print(ans * 2 ** m)
