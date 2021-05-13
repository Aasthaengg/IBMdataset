n,d=map(int,input().split())
count=1
while n-(1+2*d)>0:
    n-=(1+2*d)
    count+=1
print(count)