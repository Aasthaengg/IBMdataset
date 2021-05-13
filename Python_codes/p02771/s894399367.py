a,b,c = input().split()

if a!=b and b!=c and a!=c:
    print("No")
elif a==b and b==c and a==c:
    print("No")
else:
    print("Yes")