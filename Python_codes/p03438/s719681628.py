n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
su=0
c=[]
for i in range(n):
    x=a[i]-b[i]
    if x>=0:
        su += x
    else:
        c.append(-x)
cap=0
for i in range(len(c)):
    cap += c[i]//2
if cap>=su:
    print('Yes')
else:
    print('No')