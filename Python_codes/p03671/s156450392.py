INPUT = list(map(int,input().split()))
a=INPUT[0]
b=INPUT[1]
c=INPUT[2]
print(min(a+b,b+c,c+a))
