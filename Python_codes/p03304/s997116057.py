n,m,d=map(int,input().split())
p = ((n - d) * 2) / (n * n);
if d == 0: p /= 2
ans = p * (m - 1)
print(ans)
