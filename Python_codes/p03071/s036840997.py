a,b=map(int,input().split())
sum=0
if a > b:
    sum+=a
    if (a-1) > b:
        sum+=(a-1)
    elif (a-1)<b:
        sum+=b
    else:
        sum+=(a-1)
elif a < b:
    sum+=b
    if a < (b-1):
        sum+=(b-1)
    elif a > (b-1):
        sum+=a
    else:
        sum+=(b-1)
else:
    sum=a+a
print(sum)