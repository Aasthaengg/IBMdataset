a,b,k=map(int,input().split())
for i in range(k):
    if i%2==0:
        if a%2!=0:
            a-=1
        a=1/2*a
        b=b+a
    else:
        if b%2!=0:
            b-=1
        b=1/2*b
        a=a+b
print(int(a),int(b))