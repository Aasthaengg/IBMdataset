money = int(input())
one = int(input())
while money / 500 >= 1:
    money -= 500
if money <= one:
    print("Yes")
else:
    print("No")