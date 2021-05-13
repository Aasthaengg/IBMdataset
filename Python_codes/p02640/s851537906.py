x, y = map(int, input().split())

high = x*4
low = x*2

if low <= y <= high and y % 2 == 0:
    print("Yes")
else:
    print("No")