import fractions
a,b,c,d = map(int,input().split())
l = (c*d)//fractions.gcd(c,d)
#print(fractions.gcd(c,d))
num =(((a-1)//c)+(((a-1)//d))-((a-1)//l))
num2 =((b//c)+(b//d))-(b//l)
print(b-a-(num2-num)+1)