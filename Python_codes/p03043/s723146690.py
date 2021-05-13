import math
s = input().split()
n=int(s[0])
k=int(s[1])
ans=0
for i in range(1,n+1):
    a=math.log2(k/i)
    if a<0:
        a=0
    a=math.ceil(a)
    ans+=(1/n)*(1/2)**a

print(ans)