a,b,c=map(int,input().split())
if (a+b)+1 >= c:
    print(b+c)
else:
    print(b+c-(c-(a+b+1)))