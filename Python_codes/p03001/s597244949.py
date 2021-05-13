w, h, x, y = map(int, input().split())
multi = 1 if 2*x == w and 2*y == h else 0
print(w*h/2, multi)