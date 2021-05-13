a,b,c = map(int,input().split())
temp = 0
temp = b
b = a
a = temp
temp = a
a = c
c = temp
print(a,b,c)