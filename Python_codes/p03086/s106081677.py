a=input()
total=0
total2=0
i=0
while True:
    if i==len(a):
        break
    elif a[i]=="A" or a[i]=="T" or a[i]=="C" or a[i]=="G":
        total+=1
        i+=1
    else:
        i+=1
        if total2<total:
            total2=total
        total=0
if total2<total:
    print(total)
else:
    print(total2)