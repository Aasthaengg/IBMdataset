from math import factorial
n,p=map(int,input().split())
A=list(map(int,input().split()))

a,b=0,0
for i in A:
    if i%2==0:a +=1
    else:b +=1

cnt=0 if p==1 else 1
for i in range(p,b+1,2):
    if i==0:continue
    cnt +=factorial(b)//(factorial(i)*factorial(b-i))

print(cnt*(2**a))