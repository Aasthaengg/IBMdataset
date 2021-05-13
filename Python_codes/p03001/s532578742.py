w,h,x,y = (int(xi) for xi in input().split())

out =0
if x==w/2 and y==h/2:
    out = 1

print(w*h/2, out)
