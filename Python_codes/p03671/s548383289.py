a, b, c= list(map(int, input().split()))
x = min(a+b, a+c)
print(min(x, b+c))