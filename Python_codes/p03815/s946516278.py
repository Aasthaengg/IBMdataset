n=int(input())
a = n//11
b = n%11

if b == 0:
    print(a*2)
if 1 <= b <= 6:
    print(a*2+1)
if 7 <= b < 11:
    print(a*2+2)