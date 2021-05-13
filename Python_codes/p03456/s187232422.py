a,b = input().split()
c = int(a+b)**0.5
print("Yes" if c.is_integer() else "No")