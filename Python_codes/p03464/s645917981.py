n=int(input())
a=list(map(int,input().split()))[::-1]
if a[0]!=2:
    print(-1)
    exit()
import math
#print(a)
maxi=3
mini=2
for i in range(1,n):
    if mini<=a[i]:
        mini=a[i]
    else:
        times=math.ceil(mini/a[i])
        mini=a[i]*times
    if mini>maxi:
        print(-1)
        exit()
    #print("i={} mini={}".format(i,mini))
    if maxi<a[i]:
        print(-1)
        exit()
    else:
        times=int(maxi/a[i])
        maxi=a[i]*(times+1)-1
    #print("i={} maxi={}".format(i,maxi))
print(mini,maxi)