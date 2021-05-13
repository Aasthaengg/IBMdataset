a,b,k=map(int,input().split())
flag=0
if k%2==1:
    flag=1
for i in range(k//2):
    if a%2==1:
        a=a-1
    b+=(a/2)
    a=a/2
    if b%2==1:
        b=b-1
    a+=(b/2)
    b=b/2
if flag==1:
    if a%2==1:
        a=a-1
    b+=(a/2)
    a=a/2
print(int(a),int(b))