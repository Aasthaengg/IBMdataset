a,b,c=map(int,input().split())
k=int(input())
if a<b and c>b:
    exit(print("Yes"))
while(b<=a and k>0):
    b*=2
    k-=1
while(c<=b and k>0):
    c*=2
    k-=1
if a<b and c>b:
    print("Yes")
else: print("No")