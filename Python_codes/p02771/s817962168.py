a, b, c = map(int, input().split())
if a == b:
    if a != c:
        print("Yes")
    else:
        print("No")
elif a == c:
    print("Yes")
elif b == c:
    print("Yes")
else:
    print("No")