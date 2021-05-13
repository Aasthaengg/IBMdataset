a, b = map(int, input().split())
x = 2*(max(a,b))-1
y = a+b
print(x if x > y else y)