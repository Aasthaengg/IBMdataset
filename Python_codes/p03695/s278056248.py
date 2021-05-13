n=int(input())
a=list(map(int,input().split()))

i=0
f1=f2=f3=f4=f5=f6=f7=f8=f9=0

while i<n:

    if 1<=a[i]<=399:

        f1=1

    elif 400<=a[i]<=799:

        f2=1

    elif 800<=a[i]<=1199:

        f3=1

    elif 1200<=a[i]<=1599:

        f4=1

    elif 1600<=a[i]<=1999:

        f5=1

    elif 2000<=a[i]<=2399:

        f6=1

    elif 2400<=a[i]<=2799:

        f7=1

    elif 2800<=a[i]<=3199:

        f8=1

    elif 3200<=a[i]:

        f9+=1

    i+=1

if f1==f2==f3==f4==f5==f6==f7==f8==0 and f9!=0:
    ans1=1
else:
    ans1 = f1+f2+f3+f4+f5+f6+f7+f8

ans2 = f1+f2+f3+f4+f5+f6+f7+f8+f9

print(str(ans1)+' '+str(ans2))