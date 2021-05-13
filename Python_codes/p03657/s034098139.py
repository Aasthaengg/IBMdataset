a,b =(input().split())
a = int(a)
b = int(b)
soma = a + b
if a % 3 == 0:
    print ('Possible')
elif b % 3 == 0:
    print ('Possible')
elif soma % 3 == 0:
    print ('Possible')
else:
    print ('Impossible')