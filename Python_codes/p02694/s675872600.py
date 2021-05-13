from math import floor
X=int(input())
ans=100
count=0
while ans<X:
    ans=ans+floor(ans//100)
    count+=1
print(count)