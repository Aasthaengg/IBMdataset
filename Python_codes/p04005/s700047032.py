a,b,c=map(int,input().split())
print(0 if (a*b*c)%2==0 else min(a*b,b*c,c*a))