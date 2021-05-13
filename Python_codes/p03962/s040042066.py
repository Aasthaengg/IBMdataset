a, b, c = map(int, input().split())

if (a==b and b==c):
    print("1")

elif (a==b and b!=c):
    print("2")

elif (a!=b and b==c ):
    print("2")

elif (a==c and b!=c):
    print("2")

elif (a!=c and b==c):
    print("2")

else: print("3")
