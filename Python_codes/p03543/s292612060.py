str = input()
a = int(str[:3])
b = int(str[-3:])
print("Yes") if a % 111 == 0 or b % 111 == 0 else print("No")