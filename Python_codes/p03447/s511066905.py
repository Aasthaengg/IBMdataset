# A - Buying Sweets
x=int(input())
a=int(input())
b=int(input())

d=x-a
if d<=0:
    print(0)
    exit()

print(d%b)
