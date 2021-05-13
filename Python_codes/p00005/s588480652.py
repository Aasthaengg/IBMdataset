import sys

ary=[]
ans=[]
def gcd(a,b):
    x=sorted([a,b])
    while x[1]%x[0]!=0:
        dif=x[1]%x[0]
        x[1]=x[0]
        x[0]=dif
    return x[0]
for i in sys.stdin:
    ary.append(list(map(int,i.split())))
    ans.append([gcd(*ary[-1]),int(ary[-1][0]*ary[-1][1]/gcd(*ary[-1]))])
for i in range(len(ans)):
    print('{0:d} {1:d}'.format(*ans[i]))