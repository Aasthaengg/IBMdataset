w, h, x, y = list(map(int, input().split()))

a = w*h/2
m = "1" if (x==w/2) and (y==h/2) else "0"

print(str(a) + " " + m)