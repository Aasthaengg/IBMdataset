line = input()
a, b = [int(n) for n in line.split()]
soma, mult, minus = a+b, a*b, a-b 
if(soma > mult and soma > minus):
    print(soma)
elif(mult > minus):
    print(mult)
else:
    print(minus)