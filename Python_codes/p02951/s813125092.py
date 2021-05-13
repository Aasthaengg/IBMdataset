A=list(map(int,input().split()))
a=A[0]
b=A[1]
c=A[2]
if c-(a-b)>=0:
    print(c-(a-b))
else:
    print(0)