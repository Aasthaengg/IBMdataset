a,b = map(int,input().split())
c = (a+b)//2
print(c if (a+b)%2==0 else c+1)