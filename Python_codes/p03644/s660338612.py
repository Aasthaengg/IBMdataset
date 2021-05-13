a=int(input())
b=1
total2=0
for i in range(1,a+1):
    total=0
    a=i
    while True:
        if a%2==0:
            a=a/2
            total+=1
        else:
            if total2<total:
                total2=total
                b=i
            break
print(b)      