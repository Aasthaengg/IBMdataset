a, b = map(int, input().split())
tmp = max(a-b,a*b)
print(max(a+b,tmp))