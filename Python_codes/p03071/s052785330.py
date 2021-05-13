a,b=map(int,input().split())
if a<b:
    ct=b
    b-=1
else :
    ct=a
    a-=1
if a<b:
    ct+=b
else:
    ct+=a
print(ct)