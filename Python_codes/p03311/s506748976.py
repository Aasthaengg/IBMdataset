from numpy import*
n=int(input())
a=array(list(map(int,input().split())))
b=a-arange(1,n+1)
c=median(b)
d=abs(b-c).sum()
print(int(d))