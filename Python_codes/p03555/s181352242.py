a=input()
b=input()

if (a[0] == b[-1]) and (a[1] == b[-2]) and (a[2] == b[-3]):
    print("YES")
else:
    print("NO")