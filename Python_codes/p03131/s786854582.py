import sys
k,a,b=map(int, input().split())
if a>=b or (a<b and b-a==1):
    bis=1+k
    print(bis)
    sys.exit()
if a<b and (k-a+1)%2==0:
    bis=(b-a)*((k-a+1)//2-1)+b
    print(bis)
    sys.exit()
if a<b and (k-a+1)%2!=0:
    bis=(b-a)*((k-a+1)//2-1)+b+1
    print(bis)