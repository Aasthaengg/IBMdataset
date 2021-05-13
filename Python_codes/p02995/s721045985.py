import fractions
A,B,C,D = map(int,input().split())
#(B-B以下のCorDの倍数)-(A-1-A-1以下のCorDの倍数)
l = C*D//fractions.gcd(C,D)
x = B-(B//C+B//D-B//l)
y = (A-1)-((A-1)//C+(A-1)//D-(A-1)//l)
print(x-y)