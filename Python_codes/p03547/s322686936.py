a = list(map(str,input().split()))
if a[0] == a[1]:
    print("=")
    exit()
b = sorted(a)
if a == b:
    print("<")
else:
    print(">")

