w,h,x,y  = map(int,input().split())

print(float(w)*float(h)/2,1 if x+x == w and y+y == h else 0)