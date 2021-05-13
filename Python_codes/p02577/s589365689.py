num = input()
total = 0
for char in num:
    total = (total + int(char)) % 9
if total == 0:
    print("Yes")
else:
    print("No")