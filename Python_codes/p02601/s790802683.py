a,b,c = [int(x) for x in input().split(' ')]
k = int(input())
z=0
while(a>=b):
    b*=2
    z+=1
while (b>=c):
    c*=2
    z+=1
if(z<=k):
    print("Yes")
else:
    print("No")
