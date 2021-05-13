# from math import ceil,sqrt,log,gcd,pi
# def ii():return int(input())
# def si():return input()
# def mi():return map(int,input().split())
# def li():return list(mi())

# for _ in range(ii()):
a,b=map(int,input().split())
s=(a+b)
if(s==0 or s%2):
    print("IMPOSSIBLE")
else:
    x=0
    if(s!=0):
        x=abs(s)//2
    print(x)