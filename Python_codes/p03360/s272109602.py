a,b,c = map(int, input().split())
k = int(input())

n = max(a, b)
n = max(n, c)

ans = a+b+c+n*(2**k-1)

print(ans)