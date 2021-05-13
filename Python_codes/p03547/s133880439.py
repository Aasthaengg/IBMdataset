a=[i for i in input().split()]
if a[0]==a[1]:
    print("=")
elif a==sorted(a):
    print("<")
else:
    print(">")