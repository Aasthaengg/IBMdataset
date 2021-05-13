p=['a','b','c']
l=[list(input()) for _ in range(3)]
x=0
while True:
    if l[x]==[]:break
    x=p.index(l[x].pop(0))
print(p[x].upper())