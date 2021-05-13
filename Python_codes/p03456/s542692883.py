a,b  = input().strip().split()
l=len(b)
a, b = [int(a), int(b)]
c=(10**l)*a+b
d=c**0.5-c**0.5%1
if d**2==c:
    print("Yes")
else:
    print("No")