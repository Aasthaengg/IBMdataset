a, b, c = map(int, input().split())

if c - a - b > 0:
    if 4*a*b < c*c + (a + b)*(a + b - 2*c):
        print("Yes")
        exit()

print("No")