n, m = map(int, input().split())

ans = 1900 * m + (n-m) * 100
ans /=  0.5 ** m

print(int(ans))