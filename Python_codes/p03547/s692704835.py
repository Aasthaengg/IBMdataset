X,Y=input().split()
d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
if d[X]<d[Y]:
    print('<')
elif d[Y]<d[X]:
    print('>')
else:
    print('=')