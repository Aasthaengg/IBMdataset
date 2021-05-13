a=list(map(int,input().split()))
b=sorted(a)
c=b[::-1]
d=10*c[0]+c[1]
print(d+b[0])