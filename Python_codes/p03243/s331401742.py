n = int(input())
a = n//100
b = 100*a+10*a+a
if b >= n:
    print(b)
else:
    print(b+111)