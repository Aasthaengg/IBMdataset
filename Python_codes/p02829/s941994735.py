a=int(input())
b=int(input())
c=[1,2,3]
c.pop(c.index(a))
c.pop(c.index(b))
print(c[0])