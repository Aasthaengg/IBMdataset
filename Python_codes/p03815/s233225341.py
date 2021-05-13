x = int(input())
y = x % 11
z = x // 11
if 0 <  y  <= 6:
    print(2*z + 1)
elif y == 0:
    print(2*z)
elif 7 <= y <= 11:
    print(2*z +2 )