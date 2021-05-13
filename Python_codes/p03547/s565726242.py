x = list(map(str, input().split()))
a = int(x[0],16)
b = int(x[1],16)
if a < b:
    print('<')
elif a == b:
    print('=')
else:
    print('>')