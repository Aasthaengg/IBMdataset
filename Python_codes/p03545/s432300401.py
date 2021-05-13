n=int(input())
d=n%10
c=(n//10)%10
b=(n//100)%10
a=n//1000

for i in range(8):
    k=[1,1,1]
    for j in range(3):
        if ((i>>j)&1):
            k[j]=-1
    if a+k[0]*b+k[1]*c+k[2]*d==7:
        for j in range(3):
            if k[j]==1:
                k[j]="+"
            else:
                k[j]="-"
        print(str(a)+k[0]+str(b)+k[1]+str(c)+k[2]+str(d)+"=7")
        break
