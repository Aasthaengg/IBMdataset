import math
#=input()
#=int(input())
a,b,c=map(int,input().split())
#=map(str,input().split())
#=list(map(int,input().split()))
if 4*a*b < (-a-b+c)**2 and a+b<=c:
    print("Yes")
else:
    print("No") 