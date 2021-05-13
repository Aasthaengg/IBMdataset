n = int(input())
a = int(input())
nd5 = n//500
f = False
if nd5*500+a >= n:
    f = True
print("Yes") if f else print("No")