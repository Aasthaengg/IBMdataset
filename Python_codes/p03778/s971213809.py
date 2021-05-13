W, a, b = map(int, input().split())
if (a > b):
    a_left = a
    b_right = b + W
    if (b_right >= a_left):
        print("0")
    else:
        ans = a_left - b_right
        print(ans)
else:
    b_left = b
    a_right = a + W
    
    if (a_right >= b_left):
        print("0")
    else:
        ans = b_left - a_right
        print(ans)
