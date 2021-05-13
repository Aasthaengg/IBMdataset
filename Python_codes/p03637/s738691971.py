n=int(input())
a=list(map(int,input().split()))
i4=0
i2=0
i0=0
for x in a:
    if x%4==0:i4+=1
    elif x%2==0:i2+=1
    else:i0+=1
if i4>=i0:print("Yes")
elif i4+1==i0 and i2==0:print("Yes")
elif i0==0:print("yes")
else:print("No")