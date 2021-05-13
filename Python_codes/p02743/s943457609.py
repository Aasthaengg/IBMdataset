a, b, c = map(int, input().split())
if c - a - b <= 0:
    print("No")
    exit()
print("Yes") if 4*a*b < (c-a-b)*(c-a-b) else print("No")