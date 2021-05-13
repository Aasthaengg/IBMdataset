a,b,x=map(int, input().split())

MIN=a+(x-a%x)%x
#print(MIN)
if MIN>b:
    print(0)
else:
    print(1+(b-MIN)//x)