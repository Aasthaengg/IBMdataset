n,a,b = map(lambda x: int(x), input().split())
x = list(map(lambda x: int(x), input().split()))
last = x[0]
ans = 0
for i in x:
    diff = i - last
    last = i
    ans += min(diff*a,b)
print(ans)