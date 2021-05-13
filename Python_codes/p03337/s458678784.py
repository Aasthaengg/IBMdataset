a, b=map(int, input().split())
temp=a+b
if(a*b)>temp:
    temp=a*b
if(a-b)>temp:
    temp=a-b
print(temp)
