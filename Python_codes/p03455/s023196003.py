a,b = map(int, input().split())

if a % 2 != 0:
    if b % 2 != 0:
        print("Odd")
    else:
        print("Even")
else:
    print("Even")
