a=100000
n=int(input())

for i in range(n):
    a=a*1.05
    b=a%1000
    c=a//1000
    if b==0 :
        a=int(a)
    else:
        a=int(c*1000+1000)
print(a)
