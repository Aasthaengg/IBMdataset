n = int(input())
import math

nn = math.factorial(n)

if n ==1:
    print(1)
    
elif n ==2:
    print(2)
else:
    sosu =[2]  
   
    for i in range(3,n+1,2):
        judge = 0
        for j in range(2,i):
            if i % j == 0:
                judge = 1
        if judge ==0:
            sosu.append(i)
    
    slist =[0]*len(sosu)
    for k in range(0,len(sosu)):
        m = nn
        count = 0
        while m % sosu[k] ==0:
            m = m //sosu[k]
            count +=1
        slist[k] = count
    
    res = 1
    for l in range(0,len(slist)):
        res =res*(slist[l]+1) % 1000000007

    print(res)