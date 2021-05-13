a,b = [int(x) for x in input().split()]
ans = max([a+b, a-b, a*b])
print(ans)