a,s,d=map(int,input().split())
S=(a+s+d)//2
print(int((S*(S-a)*(S-s)*(S-d))**(1/2)))