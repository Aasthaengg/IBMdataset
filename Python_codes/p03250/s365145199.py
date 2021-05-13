a,b,c = map(int, input().split())
ans = max(10*a+b+c, 10*b+a+c, 10*c+a+b)
print(ans)