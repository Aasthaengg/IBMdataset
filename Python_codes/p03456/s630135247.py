a,b=input().split()
c=a+b
c=int(c)
print("Yes" if c**(1/2)%1==0 else "No")