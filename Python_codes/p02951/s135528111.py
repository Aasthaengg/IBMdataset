def inp():return map(int,input().split())
a,b,c=inp()

c=c-(a-b)
print(max(0,c))