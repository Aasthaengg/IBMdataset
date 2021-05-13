a,b,c=map(int,input().split())
print(b+c if c<=(a+b) else a+b*2+1)