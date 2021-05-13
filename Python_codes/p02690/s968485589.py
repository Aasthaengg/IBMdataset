x=int(input())
a=0
b=0
for i in range(1000):
    for j in range(1000):
        if i**5-j**5==x:
            a=i
            b=j
            break
        elif i**5+j**5==x:
            a=i
            b=-j
            break
    if a!=0 or b!=0:
        break
print(str(a)+" "+str(b))