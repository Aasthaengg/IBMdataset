import sys
# print ("Enter length and width")
a,b=map(int,sys.stdin.readline().split())
area=a*b;
peri=a+a+b+b;
print(area,peri)

