
import math

x=1234

def divmod2(x,y):
    a=math.floor(x/y)
    b=x%y
    return x,y

def ksouwa(x):
    x=int(x)
    sen=math.floor(x/1000)
    hyaku=math.floor((x%1000)/100)
    juu=math.floor((x%100)/10)
    iti=math.floor(x%10)
    return sen+hyaku+juu+iti

def ksouwa2(x):
    int1=0
    x=str(x)
    len(x)
    for i in list(x):
        #print(i)
        int1=int(int1)+int(i)
    return int1

X,A,B=open(0).read().split()

X=int(X)

A=int(A)

B=int(B)

int1=0
int2=0

for i in range(X+1):
    if (ksouwa2(i)>=A) and (ksouwa2(i)<=B):
        int1=int1+1
        int2=int2+i

#print(int1)
print(int2)