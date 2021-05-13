a,b,c = map(int, input().split())
k = int(input())

if (a>=b and a>=c) :
    for i in range(k):
        a *= 2
elif (b>a and b>=c):
    for i in range(k):
        b *= 2
else: 
    for i in range(k):
        c *= 2
print(a+b+c)