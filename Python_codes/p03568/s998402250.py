n=int(input())
a=list(map(int,input().split()))

num=pow(3,n)

temp=1
for i in a:
    if i%2==0:
        temp*=2

print(num-temp)