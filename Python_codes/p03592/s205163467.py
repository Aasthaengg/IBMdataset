h,w,k = map(int,input().split())
for x in range(1001):
    for y in range(1001):
        if w*x + h*y - 2*x*y == k and 0<= x <= h and 0<= y <= w:
            print("Yes")
            exit()
print("No")