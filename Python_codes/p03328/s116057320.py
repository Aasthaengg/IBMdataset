import sys
a,b = map(int,input().split())

if not (1 <= a <= b <= 499500):
    sys.exit()

b_hight = 0
for I in range(1,(b - a + 1)):
    b_hight += I

print(b_hight - b)