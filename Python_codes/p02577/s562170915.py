num = input()

ans = 0

for digit in num:
    ans += int(digit)

if ans % 9 == 0:
    print("Yes")

else:
    print("No")