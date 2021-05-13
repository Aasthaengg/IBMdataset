x,y = map(int,input().split())

c=x
a=[]
while c <= y:
    a.append(c)
    c *=2
    
print(len(a))