import math
n=int(input())
cnt=0
for i in range(1,int(math.sqrt(n)+1))[::-1]:
    if n%i==0:
        cnt=i
        break
a=n/cnt
b=a+cnt-2
print(int(b))
