a, b, c = map(int, input().split())

if (a >= 0 and a <= 100) and (b >= 0 and b <= 100) and (c >= 0 and c <= 100):
    if a < b < c:
        print("Yes", end="\n")
    else:
        print("No", end="\n")