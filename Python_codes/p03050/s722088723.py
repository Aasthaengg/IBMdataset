n=int(input())


s=0
a=1
while a*a+a<n:
    if n%a==0:
        s+=n//a-1
    a+=1

print(s)