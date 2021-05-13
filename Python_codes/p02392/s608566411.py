while True:
    a, b, c = map(int, input().split())
    if a >= 0 and a <= 100:
        if b >= 0 and b <= 100:
            if c >= 0 and c <= 100:
                break

if a < b and b < c:
    print("Yes")
else :
    print("No")
