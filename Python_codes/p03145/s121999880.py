a, b, c = map(int, input().split())
dai = max(a,b,c)
shou = min(a,b,c)
mid = a + b + c - dai - shou

print(shou * mid // 2)
