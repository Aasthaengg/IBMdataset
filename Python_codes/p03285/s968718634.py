n=int(input())
flag=False
for i in range(int(n/4)+1):
    for j in range(int(n/7)+1):
        if(i*4+j*7==n):
            flag=True

if(flag==True):
    print("Yes")
else:
    print("No")
