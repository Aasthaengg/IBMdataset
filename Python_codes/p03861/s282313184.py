a,b,x = map(int,input().split())
if a != 0:
    dum1 = ((a-1) // x) + 1
else:
    dum1 = 0
dum2 = (b//x)+1
print(dum2-dum1)
