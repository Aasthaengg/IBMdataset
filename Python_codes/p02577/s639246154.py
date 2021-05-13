n = input()
sum = 0
for i in n:
    sum += int(i)
    sum %= 9
if sum%9 != 0:
    print("No")
else:
    print("Yes")
