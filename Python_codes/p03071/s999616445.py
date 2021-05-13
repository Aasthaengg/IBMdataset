a,b=map(int,input().split())
max=a+b
if a+a-1>max:
    max=a+a-1
if b+b-1>max:
    max=b+b-1
print(max)