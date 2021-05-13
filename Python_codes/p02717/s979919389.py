a,b,c = map(int,input().split())
d = a
a = b
b = d
d = c
c = a
a = d
print(a,b,c)