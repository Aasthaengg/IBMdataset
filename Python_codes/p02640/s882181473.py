x,y = list(map(int,input().split()))
if (-(-y//4)) <= x and y % 2 == 0 and y // 2 >= x:
    print("Yes")
else:
    print("No")