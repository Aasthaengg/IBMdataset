n, m = map(int, input().split())
l = pow(2, m)
ans = 100*(n-m)*l + 1900*m*l
print(ans)