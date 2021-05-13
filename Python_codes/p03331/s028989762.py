n = int(input())

if n%10 == 0 and n != 10:
    print(10)
else:
    a,b = 1,0
    sA, sB= 0,0
    soma = []

    while a<=n:
        b=n-a

        for i in str(a):
            sA+=int(i)
        for j in str(b):
            sB+=int(j)
        soma.append(sA+sB)
    
        a=a+1
    print(min(soma))
