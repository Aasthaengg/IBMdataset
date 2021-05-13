W, H, x, y = [int(x) for x in input().split()]

max_value = W*H/2
flg = W-x == x and H-y == y 
print(max_value, 1 if flg else 0)