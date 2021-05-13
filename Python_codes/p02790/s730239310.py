a,b = list(input().split())
x = a*int(b)
y = b*int(a)
list = [x,y]
list.sort()
print(list[0])