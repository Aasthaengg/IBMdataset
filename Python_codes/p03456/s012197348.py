a, b = map(str, input().split())

c = a + b

if (int(c)**(1/2)).is_integer():
    print("Yes")
else:
    print("No")