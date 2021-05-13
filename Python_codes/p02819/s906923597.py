x=int(input())
flag=1
prime=[]
num=2
while flag!=0:
    f=0
    for p in prime:
        if num%p==0:
            f=1
            break
    if f==0:
        prime.append(num)
        if x<=num:
            flag=0
    if flag==0:
        break
    else:
        num+=1
print(num)
