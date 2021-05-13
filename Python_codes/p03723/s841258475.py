A,B,C=map(int,input().split())

cnt=0
lp=0
ls=set()
a=A
b=B
c=C
ls.add((a,b,c))
while not(a%2==1 or b%2==1 or c%2==1 or lp==1):
    a=int((A+B+C-a)/2)
    b=int((A+B+C-b)/2)
    c=int((A+B+C-c)/2)
    cnt+=1
    if ((a,b,c) in ls):
        lp=1
if lp==1:
    print(-1)
else:
    print(cnt)