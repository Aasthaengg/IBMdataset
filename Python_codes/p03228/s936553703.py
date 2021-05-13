a,b,k=map(int,input().split())
flg=True
for i in range(k):
    if flg:
        a//=2
        b+=a
        flg=False
    else:
        b//=2
        a+=b
        flg=True
print(a,b)