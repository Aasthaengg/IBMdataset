a,b,c=input().split()
a = eval(a)
b = eval(b)
c = eval(c)
if (c < a + b):
    print("No")
elif 4*a*b<pow(c-a-b,2):
    print("Yes")
else:
    print("No")
