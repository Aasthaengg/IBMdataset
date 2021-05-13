n = int(input())
if n < 10:
    x = n
elif n < 100:
    x = 9
elif n < 1000:
    x = n - 90
elif n < 10000:
    x = 909
elif n == 100000:
    x = 90909
else:
    x = n - 9090
print(x)