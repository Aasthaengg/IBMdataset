a,b = map(int, input().split())
ret = max(a+b, a-b, a*b)
print(ret)
