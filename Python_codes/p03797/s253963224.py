n , m = map(int, input().split())
ans = 0
ans += min(n,m//2)
if m-2*n>0:
    ans+=(m-2*n)//4
print(ans)
