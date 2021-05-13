a, b, c = map(int, input().split())

if a < b:
    if a < c:
        if b < c:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")