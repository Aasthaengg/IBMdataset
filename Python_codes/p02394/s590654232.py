num = list(map(int, input().split()))

W = num[0]
H = num[1]
x = num[2]
y = num[3]
r = num[4]

if(( x + r <= W ) and ( x - r >= 0 ) and (y + r <= H) and (y - r >= 0)):
    print("Yes")
else:
    print("No")