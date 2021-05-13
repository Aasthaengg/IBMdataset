inpstr=input()
inpint=int(inpstr)
count=0
while inpint !=0:
    if len(str(inpint))%2==1:
        count+=1
    inpint-=1
print(count)