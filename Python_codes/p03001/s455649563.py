w,h,x,y = map(int, input().split())

pw = w/2
ph = h/2

print(w*h/2, 1 if(pw == x and ph == y) else 0)
