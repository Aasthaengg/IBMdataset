a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a >= b)and(c >= d):
    print(b + d)
elif(a >= b)and(c <= d):
    print(b + c)
elif(a <= b)and(c <= d):
    print(a + c)
else:
    print(a + d)