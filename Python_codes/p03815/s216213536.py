x = int(input())
p = int(x/11)
x -= p*11
if x == 0:
    print(2*p)
elif x >6:
    print(2*p+2)
else:
    print(2*p+1) 