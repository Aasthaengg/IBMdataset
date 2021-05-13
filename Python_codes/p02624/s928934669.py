def g(n):
    ans = (n*(n+1))//2
    return ans

N = int(input())
ans = 0

for i in range(1,N+1):
    ans += (i*g(N//i))

print(ans)
