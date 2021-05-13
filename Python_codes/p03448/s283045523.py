a=int(input()) #50*10*a
b=int(input()) #50*2*b
c=int(input()) #50*1*c
x=int(input())

#xは50の何倍？？
m=x//50
count=0
#m=10*a+2*b+cなる整数a,b,cの組

for i in range(0,a+1):
    for j in range(0,b+1):
        for k in range(0,c+1):
            if 10*i+2*j+k==m:
                count+=1
            
print(count)