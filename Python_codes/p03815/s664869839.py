x=int(input())
if x<=6:
    print(1)
elif x<=11:
    print(2)
elif x%11==0:
    print(2*(x//11))
elif x%11<=6:
    print(2*(x//11)+1)
else:
    print(2*(x//11)+2)