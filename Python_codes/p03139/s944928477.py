n,a,b = map(int, input().split())
if a+b > n: x = (a+b)-n
else: x = 0
print(min(a,b), x)