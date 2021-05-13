A,B = map(int, input().split())
list = []
a = A + B
b = A - B
c = A * B
list = list + [a,b,c]
print(max(list))
