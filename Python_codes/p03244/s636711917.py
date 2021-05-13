from collections import Counter

n=int(input())
a=list(map(int,input().split()))

if a.count(a[0])==n:
    print(n//2)
    exit()


x=a[::2]
y=a[1::2]

xx=Counter(x)
yy=Counter(y)

xxx=xx.most_common()
yyy=yy.most_common()

if xxx[0][0]!=yyy[0][0]:
    print(n-xxx[0][1]-yyy[0][1])

else:
    print(min(n-xxx[1][1]-yyy[0][1],n-xxx[0][1]-yyy[1][1]))
