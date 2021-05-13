n,a,b = map(int,input().split())
xl = list(map(int,input().split()))

ans = 0
for i in range(n-1):
    diff = xl[i+1] - xl[i]
    ans += min(diff*a,b)

print(ans)