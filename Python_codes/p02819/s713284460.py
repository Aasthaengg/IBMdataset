import math
s=int(input())
def sosuuukana(x):
    y=int(math.sqrt(x))
    f=0
    for i in range(2,y+1):
        if x%i==0:
            f=f+1
            break
    return f
while sosuuukana(s)>0:
    s=s+1
else:
    print(s)