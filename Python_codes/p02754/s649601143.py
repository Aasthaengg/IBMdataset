n,a,b = map(int,input().split())
ans = 0
ans += (n // (a+b)) * a
n %= a+b
ans += min(a,n)
print(ans)