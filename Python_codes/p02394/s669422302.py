w,h,x,y,r = map(int,input().split())

print("No") if x-r<0 or y-r<0 or x+r>w or y+r>h else print("Yes")