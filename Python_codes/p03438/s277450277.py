import math
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=sum(b)-sum(a)
d=0
for i in range(n):
 if a[i]>b[i]:d+=a[i]-b[i]
 elif a[i]%2!=b[i]%2:d+=1
print("No"if c<d else"Yes")