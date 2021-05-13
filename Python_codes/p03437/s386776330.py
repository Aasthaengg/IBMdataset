a,b=map(int,input().split())
c=a*b+a
print(c if c%b!=0 else -1)