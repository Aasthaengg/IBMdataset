red, blue = input().split()
red_num, blue_num = list(map(int, input().split()))
s = input()

if s == red:
    red_num -= 1
elif s == blue:
    blue_num -= 1

print(str(red_num) + ' ' + str(blue_num))