a=list(map(int,input().split()))
b=list(map(int,input().split()))
no=1
for i in range(1,a[0]):
    b[i]+=b[i-1]
for i in range(0,a[0]):
    if(a[1]>=b[i]):
        no+=1
    else:
        break
print(no)        