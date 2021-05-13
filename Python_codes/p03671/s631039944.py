a,b,c = map(int,input().split())
list = [a, b, c]
x = min(list)
list.remove(x)
y = min(list)
print(x + y)
