w, h, x, y = map(int, input().split())

s = w*h/2 
ans = int((w/2, h/2) == (x, y))
print(s, ans)
