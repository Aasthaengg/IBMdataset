n=int(input())
a=list(map(int,input().split()))
aset=set(a)
ans=1
if len(aset)>1:
    num1=a[0]
    num2=a[1]
    num3=2 #Ai<Ai+1 1  Ai>Ai+1 0
    if num1<num2:
        num3=1
    if num1>num2:
        num3=0
    for i in range(len(a)-2):
        num=a[2+i]
        if num3==2 and num2>num:
            num3=0
        if num3==2 and num2<num:
            num3=1
        if num3==0 and num2<num:
            ans+=1
            num3=2
        if num3==1 and num2>num:
            ans+=1
            num3=2
        num2=num
print(ans)
