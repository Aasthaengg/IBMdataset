a,b = map(str,input().split())
c = int(a+b)
d = c**0.5
if d.is_integer():
    print("Yes")
else:
    print("No")
