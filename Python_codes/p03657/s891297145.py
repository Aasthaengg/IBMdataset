a,b=map(int,input().split())
f=a%3==0 or b%3==0 or (a+b)%3==0
print("Possible" if f==True else "Impossible")