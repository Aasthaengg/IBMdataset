n=int(input())
k=int(input())

tmp=1
num=1
while n>0:
    if tmp<k:
        num*=2
        tmp*=2
    else:
        num+=k
    n-=1

print(num)