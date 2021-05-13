n = int(input())
if n < 3:
    print (0)
elif n == 3:
    print (1)
else:
    a = n//3
    print (a-1) if n-a <= 2 else print (a)
