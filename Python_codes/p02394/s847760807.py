w,h,x,y,r=map(int, input().split())
print("{0}".format("Yes" if 0 <= x-r and 0 <= w-x-r and 0 <= y-r and 0 <= h-y-r else "No"))