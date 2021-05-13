n,m = map(int,input().split())
ans = 0

if n >= m//2:
    ans = m//2
else:
    ans = n + (m//2-n)//2

print(ans)
