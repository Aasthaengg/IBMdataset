n,k = map(int, input().split())
x = (n+1)//2
bl = (x>=k)
ans = 'YES' if bl else 'NO'
print(ans)