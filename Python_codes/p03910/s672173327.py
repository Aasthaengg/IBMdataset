n,ans,i = int(input()),0,1
while ans<n:
    ans+=i
    i+=1
#print("{},{}".format(ans,i))
if ans==n:
    for j in range(i-1):
        print(j+1)
else:
    i-=1
    while i>=1:
        if n==0:
            break
        if n>=i:
            print(i)
            n-=i
        i-=1