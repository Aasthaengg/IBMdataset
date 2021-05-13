li = list(map(int,input().split()))
a=li[0]
b=li[1]
k=li[2]

for i in range(1,k+1):
    if i%2==1:
        if a%2==0:
            a=a/2
            b=b+a
        else:
            a=(a-1)/2
            b=b+a
    else:
        if b%2==0:
            b=b/2
            a=a+b
        else:
            b=(b-1)/2
            a=a+b
print(int(a),int(b))
