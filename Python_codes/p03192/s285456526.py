n = int(input())
n1000 = n//1000
na = n-1000*n1000
n100 = na//100
nb=na-100*n100
n10=nb//10
nc=nb-10*n10
c = 0
if n1000 ==2:
    c += 1
if n100 ==2:
    c += 1
if n10 ==2:
    c+=1
if nc ==2:
    c+=1
print(c)
