s = int(input())
a = s%100
b = s//100

if b * 5 < a:
    print(0)
else:
    print(1)