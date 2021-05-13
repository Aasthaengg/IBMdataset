x,y=map(int,input().split())
s,t=(y-2*x)//2,(4*x-y)//2
print("Yes"if s+t==x and 4*s+2*t==y and s>=0 and t>=0else"No")